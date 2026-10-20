import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dashboard Pengunjung",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    data = pd.read_csv("dataset.csv")
    data["tanggal"] = pd.to_datetime(data["tanggal"])
    data["kelas"] = data["kelas"].str.strip()
    data["gender"] = data["gender"].str.strip()
    return data

data = load_data()

st.title("📊 Dashboard Pengunjung Perpustakaan")
st.caption(
    "Visualisasi data untuk membantu memahami pola kunjungan perpustakaan."
)

st.sidebar.header("Filter Data")

pilihan_kelas = st.sidebar.selectbox(
    "Pilih kelas",
    ["Semua"] + sorted(data["kelas"].unique().tolist())
)

pilihan_gender = st.sidebar.selectbox(
    "Pilih gender",
    ["Semua"] + sorted(data["gender"].unique().tolist())
)

data_filter = data.copy()

if pilihan_kelas != "Semua":
    data_filter = data_filter[
        data_filter["kelas"] == pilihan_kelas
    ]

if pilihan_gender != "Semua":
    data_filter = data_filter[
        data_filter["gender"] == pilihan_gender
    ]

st.subheader("Ringkasan Kunjungan")

total = len(data_filter)
laki_laki = (data_filter["gender"] == "Laki-laki").sum()
perempuan = (data_filter["gender"] == "Perempuan").sum()

if not data_filter.empty:
    kelas_terbanyak = (
        data_filter["kelas"].value_counts().idxmax()
    )
else:
    kelas_terbanyak = "-"

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Kunjungan", total)
col2.metric("Laki-laki", int(laki_laki))
col3.metric("Perempuan", int(perempuan))
col4.metric("Kelas Terbanyak", kelas_terbanyak)

st.divider()

if data_filter.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
else:
    st.subheader("Tren Kunjungan Harian")

    tren = (
        data_filter.groupby("tanggal")
        .size()
        .reset_index(name="jumlah")
    )

    fig_tren = px.line(
        tren,
        x="tanggal",
        y="jumlah",
        markers=True,
        labels={
            "tanggal": "Tanggal",
            "jumlah": "Jumlah Kunjungan"
        }
    )

    fig_tren.update_layout(
        xaxis_title="Tanggal",
        yaxis_title="Jumlah Kunjungan"
    )

    st.plotly_chart(fig_tren, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kunjungan Berdasarkan Kelas")

        per_kelas = (
            data_filter["kelas"]
            .value_counts()
            .rename_axis("kelas")
            .reset_index(name="jumlah")
        )

        fig_kelas = px.bar(
            per_kelas,
            x="kelas",
            y="jumlah",
            text="jumlah",
            labels={
                "kelas": "Kelas",
                "jumlah": "Jumlah Kunjungan"
            }
        )

        st.plotly_chart(
            fig_kelas,
            use_container_width=True
        )

    with col2:
        st.subheader("Proporsi Gender")

        per_gender = (
            data_filter["gender"]
            .value_counts()
            .rename_axis("gender")
            .reset_index(name="jumlah")
        )

        fig_gender = px.pie(
            per_gender,
            names="gender",
            values="jumlah",
            hole=0.45
        )

        st.plotly_chart(
            fig_gender,
            use_container_width=True
        )

    st.subheader("Data Kunjungan")

    tabel = data_filter.sort_values(
        "tanggal",
        ascending=False
    ).copy()

    tabel["tanggal"] = tabel["tanggal"].dt.strftime("%d-%m-%Y")

    st.dataframe(
        tabel.reset_index(drop=True),
        use_container_width=True,
        hide_index=True
    )

    csv = tabel.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Unduh Data CSV",
        data=csv,
        file_name="data_kunjungan.csv",
        mime="text/csv"
    )