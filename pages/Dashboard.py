import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.set_page_config(page_title="Spotify 2023 Dashboard", layout="wide")
st.title("Spotify 2023 Dashboard")
st.caption("Exploră cele mai populare piese din 2023 după streams și caracteristici audio.")

# ── Încărcare date ───────────────────────────────────────────────────
with st.expander("📂 Încărcare fișier CSV", expanded=False):
    fisier = st.file_uploader("Încarcă un fișier CSV Spotify", type=["csv"])

if fisier is not None:
    df = pd.read_csv(fisier, encoding="latin1", engine="python", on_bad_lines="skip")
else:
    st.sidebar.info("Nu ai încărcat un fișier. Folosesc dataset-ul local `spotify-2023.csv`.")
    st.info("Nu ai încărcat un fișier. Folosesc dataset-ul local `spotify-2023.csv`.")
    df = pd.read_csv("spotify-2023.csv", encoding="latin1", engine="python", on_bad_lines="skip")

# Ne asigurăm că coloanele numerice chiar sunt numerice
numeric_cols = [
    "in_spotify_playlists",
    "in_spotify_charts",
    "streams",
    "in_apple_playlists",
    "in_apple_charts",
    "in_deezer_playlists",
    "in_deezer_charts",
    "in_shazam_charts",
    "bpm",
    "danceability_%",
    "valence_%",
    "energy_%",
    "acousticness_%",
    "instrumentalness_%",
    "liveness_%",
    "speechiness_%",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ── Nume „user-friendly” pentru coloane ─────────────────────────────
friendly_names = {
    "track_name": "Piesă",
    "artist(s)_name": "Artist",
    "released_year": "An lansare",
    "released_month": "Lună lansare",
    "released_day": "Zi lansare",
    "streams": "Streams (total)",
    "in_spotify_playlists": "Playlist-uri Spotify",
    "in_spotify_charts": "Charts Spotify",
    "in_apple_playlists": "Playlist-uri Apple Music",
    "in_apple_charts": "Charts Apple Music",
    "in_deezer_playlists": "Playlist-uri Deezer",
    "in_deezer_charts": "Charts Deezer",
    "in_shazam_charts": "Charts Shazam",
    "bpm": "Tempo (BPM)",
    "danceability_%": "Danceability %",
    "valence_%": "Happiness / Valence %",
    "energy_%": "Energy %",
    "acousticness_%": "Acousticness %",
    "instrumentalness_%": "Instrumentalness %",
    "liveness_%": "Liveness %",
    "speechiness_%": "Speechiness %",
}

df_display = df.rename(columns=friendly_names)

# helper pentru UI
def pretty(col_name: str) -> str:
    return friendly_names.get(col_name, col_name)

# ── Filtre în pagină ────────────────────────────────────────────────
st.markdown("### 🎛️ Filtre")
filter_col1, filter_col2, filter_col3 = st.columns(3)

years = sorted(df["released_year"].dropna().unique().tolist()) if "released_year" in df.columns else []
if years:
    selected_years = filter_col1.multiselect("Ani de lansare", years, default=years, help="Filtrează piesele după anul lansării.")
else:
    selected_years = []

if "streams" in df.columns:
    min_streams = int(df["streams"].min())
    max_streams = int(df["streams"].max())
    default_min = int(df["streams"].quantile(0.75))
    min_streams_sel = filter_col2.slider(
        "Minim streams", min_value=min_streams, max_value=max_streams, value=default_min,
        help="Arată doar piesele cu streams peste acest prag."
    )
else:
    min_streams_sel = None

if "artist(s)_name" in df.columns:
    top_artists = (
        df.groupby("artist(s)_name")["streams"].sum().sort_values(ascending=False).head(15).index.tolist()
    )
    selected_artists = filter_col3.multiselect(
        "Artiști (Top 15 după streams)", options=top_artists, default=top_artists[:5],
        help="Alege rapid câțiva artiști importanți."
    )
else:
    selected_artists = []

df_filtrat = df.copy()

if selected_years and "released_year" in df_filtrat.columns:
    df_filtrat = df_filtrat[df_filtrat["released_year"].isin(selected_years)]

if min_streams_sel is not None and "streams" in df_filtrat.columns:
    df_filtrat = df_filtrat[df_filtrat["streams"] >= min_streams_sel]

if selected_artists and "artist(s)_name" in df_filtrat.columns:
    df_filtrat = df_filtrat[df_filtrat["artist(s)_name"].isin(selected_artists)]

# aplicăm același rename și pe filtrat pentru afișare în tabele
df_filtrat_display = df_filtrat.rename(columns=friendly_names)

# ── Tabs pentru explorare ────────────────────────────────────────────
tab_overview, tab_streams, tab_audio = st.tabs(["🧭 Overview", "📈 Streams & artiști", "🎧 Audio features"])

with tab_overview:
    # Statistici generale
    col1, col2, col3, col4 = st.columns(4)

    total_tracks = len(df_filtrat)
    unique_artists = df_filtrat["artist(s)_name"].nunique() if "artist(s)_name" in df_filtrat.columns else 0
    total_streams = df_filtrat["streams"].sum() if "streams" in df_filtrat.columns else 0
    avg_bpm = df_filtrat["bpm"].mean() if "bpm" in df_filtrat.columns else None

    col1.metric("Piese filtrate", total_tracks)
    col2.metric("Artiști filtrați", unique_artists)
    if total_streams > 0:
        col3.metric("Streams (miliarde)", f"{total_streams / 1e9:,.2f} B")
    else:
        col3.metric("Streams", "N/A")
    if avg_bpm:
        col4.metric("BPM mediu", f"{avg_bpm:.0f}")
    else:
        col4.metric("BPM mediu", "N/A")

    st.subheader("Primele 25 de rânduri (după filtre)")
    st.dataframe(df_filtrat_display.head(25), use_container_width=True)

with tab_streams:
    col_left, col_right = st.columns((2, 1))

    with col_left:
        st.subheader("Top 15 artiști după streams totale")
        if not df_filtrat.empty and "artist(s)_name" in df_filtrat.columns and "streams" in df_filtrat.columns:
            artist_streams = (
                df_filtrat.groupby("artist(s)_name")["streams"].sum().reset_index().sort_values("streams", ascending=False).head(15)
            )
            fig_artists = px.bar(
                artist_streams,
                x="artist(s)_name",
                y="streams",
                title="Top artiști după streams (după filtre)",
            )
            fig_artists.update_layout(
                xaxis_title=pretty("artist(s)_name"),
                yaxis_title=pretty("streams"),
                xaxis_tickangle=-45,
            )
            st.plotly_chart(fig_artists, use_container_width=True)
        else:
            st.info("Nu există suficiente date pentru a afișa topul de artiști.")

    with col_right:
        st.subheader("Top 10 piese după streams")
        if not df_filtrat.empty and "streams" in df_filtrat.columns:
            top_tracks = df_filtrat.nlargest(10, "streams")
            fig_bar = px.bar(
                top_tracks,
                x="track_name",
                y="streams",
                color="artist(s)_name",
                title="Top 10 piese după numărul de streams",
            )
            fig_bar.update_layout(
                xaxis_title=pretty("track_name"),
                yaxis_title=pretty("streams"),
                xaxis_tickangle=-45,
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Nu există suficiente date pentru a afișa graficul.")

    st.subheader("Relația între popularitate pe Spotify și alte platforme")
    if not df_filtrat.empty and "streams" in df_filtrat.columns:
        x_axis = st.selectbox(
            "Axa X (platforme / chart-uri)",
            options=[
                "in_spotify_playlists",
                "in_spotify_charts",
                "in_apple_playlists",
                "in_apple_charts",
                "in_deezer_playlists",
                "in_deezer_charts",
                "in_shazam_charts",
            ],
            index=0,
            format_func=pretty,
        )
        if x_axis in df_filtrat.columns:
            fig_scatter = px.scatter(
                df_filtrat,
                x=x_axis,
                y="streams",
                hover_name="track_name",
                color="released_year" if "released_year" in df_filtrat.columns else None,
                title=f"{pretty(x_axis)} vs. {pretty('streams')}",
            )
            fig_scatter.update_layout(
                xaxis_title=pretty(x_axis),
                yaxis_title=pretty("streams"),
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("Coloana selectată nu există în dataset.")

with tab_audio:
    st.subheader("Distribuții audio (Matplotlib)")

    if not df_filtrat.empty:
        col_a1, col_a2 = st.columns(2)

        if "bpm" in df_filtrat.columns:
            with col_a1:
                fig_hist, ax = plt.subplots(figsize=(6, 3))
                ax.hist(df_filtrat["bpm"].dropna(), bins=20, color="#ff5c00", edgecolor="white")
                ax.set_title("Distribuția BPM")
                ax.set_xlabel("BPM")
                ax.set_ylabel("Frecvență")
                st.pyplot(fig_hist)
                plt.close(fig_hist)

        if "danceability_%" in df_filtrat.columns:
            with col_a2:
                fig_dance, ax2 = plt.subplots(figsize=(6, 3))
                ax2.hist(df_filtrat["danceability_%"].dropna(), bins=20, color="#00cc96", edgecolor="white")
                ax2.set_title("Distribuția Danceability")
                ax2.set_xlabel("Danceability %")
                ax2.set_ylabel("Frecvență")
                st.pyplot(fig_dance)
                plt.close(fig_dance)

    st.markdown("---")
    st.subheader("Profil audio pentru o piesă")

    if not df_filtrat.empty and "track_name" in df_filtrat.columns:
        tracks_list = df_filtrat["track_name"].unique().tolist()
        selected_track = st.selectbox("Alege o piesă", options=tracks_list)
        track_row = df_filtrat[df_filtrat["track_name"] == selected_track].iloc[0]

        st.write(
            f"**{track_row.get('track_name', '')}** — {track_row.get('artist(s)_name', '')} "
            f"({int(track_row.get('released_year')) if 'released_year' in df_filtrat.columns and pd.notna(track_row.get('released_year')) else 'N/A'})"
        )

        # Afișăm câteva caracteristici audio sub formă de metrici
        c1, c2, c3, c4 = st.columns(4)
        for col_name, label, container in [
            ("danceability_%", "Danceability %", c1),
            ("energy_%", "Energy %", c2),
            ("valence_%", "Happiness (Valence) %", c3),
            ("acousticness_%", "Acousticness %", c4),
        ]:
            value = track_row.get(col_name)
            if pd.notna(value):
                container.metric(label, f"{value:.0f}")
            else:
                container.metric(label, "N/A")

