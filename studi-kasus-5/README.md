
# Dashboard Visualisasi Data Pengunjung Perpustakaan

## Studi Kasus

Data kunjungan perpustakaan dapat digunakan untuk memahami pola kunjungan siswa berdasarkan tanggal, kelas, dan gender. Namun, data dalam bentuk tabel terkadang sulit dipahami ketika pengguna ingin melihat tren dan membandingkan informasi secara cepat.

Proyek ini mengembangkan dashboard visualisasi data interaktif berbasis web menggunakan Python, Streamlit, Pandas, dan Plotly. Dashboard menampilkan ringkasan kunjungan, tren kunjungan harian, perbandingan jumlah kunjungan berdasarkan kelas, serta proporsi gender.

Proyek ini menerapkan konsep Human-Computer Interaction (HCI), User-Centered Design (UCD), dan Data Visualization untuk menyajikan informasi secara lebih terstruktur, interaktif, dan mudah dipahami pengguna.

Dataset yang digunakan merupakan data simulasi kunjungan siswa untuk keperluan pembelajaran.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Streamlit** — membangun dashboard interaktif berbasis web.
- **Pandas** — membaca, membersihkan, dan mengolah dataset.
- **Plotly Express** — membuat grafik interaktif.
- **Visual Studio Code** — lingkungan pengembangan program.
- **Git dan GitHub** — pengelolaan kode dan dokumentasi proyek.

## Fitur Dashboard

### 1. Ringkasan Kunjungan

Menampilkan informasi utama berdasarkan data yang sedang difilter, meliputi:

- Total kunjungan.
- Jumlah kunjungan laki-laki.
- Jumlah kunjungan perempuan.
- Kelas dengan jumlah kunjungan terbanyak.

### 2. Filter Data

Pengguna dapat menyaring data berdasarkan:

- Kelas: X, XI, XII, atau semua kelas.
- Gender: laki-laki, perempuan, atau semua gender.

Seluruh ringkasan, grafik, dan tabel akan menyesuaikan filter yang dipilih.

### 3. Grafik Tren Kunjungan Harian

Menggunakan **Line Chart** untuk menampilkan perubahan jumlah kunjungan berdasarkan tanggal sehingga pola kunjungan harian lebih mudah diamati.

### 4. Grafik Kunjungan Berdasarkan Kelas

Menggunakan **Bar Chart** untuk membandingkan jumlah kunjungan dari kelas X, XI, dan XII.

### 5. Grafik Proporsi Gender

Menggunakan **Donut Chart** untuk menunjukkan proporsi kunjungan laki-laki dan perempuan berdasarkan data yang sedang ditampilkan.

### 6. Tabel Data Kunjungan

Menampilkan data kunjungan dalam bentuk tabel yang dapat ditelusuri pengguna melalui filter yang tersedia.

### 7. Unduh Data CSV

Menyediakan tombol untuk mengunduh data hasil filter dalam format CSV agar dapat digunakan kembali untuk pengolahan atau analisis lebih lanjut.

## Dataset

Dataset disimpan dalam file `dataset.csv` dan terdiri dari 24 data simulasi kunjungan siswa.

### Struktur Dataset

| Atribut | Keterangan |
|---|---|
| `tanggal` | Tanggal kunjungan siswa. |
| `kelas` | Tingkat kelas siswa, yaitu X, XI, atau XII. |
| `gender` | Jenis kelamin siswa. |
| `waktu` | Waktu kunjungan siswa ke perpustakaan. |

### Contoh Dataset

```csv
tanggal,kelas,gender,waktu
2026-09-01,X,Perempuan,09:00
2026-09-01,XI,Laki-laki,10:00
2026-09-02,XII,Perempuan,11:00
2026-09-02,X,Laki-laki,13:00
2026-09-03,XI,Perempuan,09:30
2026-09-03,XII,Laki-laki,14:00
2026-09-04,X,Perempuan,10:30
2026-09-04,XI,Laki-laki,11:30
2026-09-05,XII,Perempuan,09:00
2026-09-05,X,Perempuan,13:30
2026-09-06,XI,Perempuan,10:00
2026-09-06,XII,Laki-laki,12:00
2026-09-07,X,Laki-laki,09:30
2026-09-07,XI,Perempuan,14:00
2026-09-08,XII,Perempuan,10:30
2026-09-08,X,Laki-laki,11:00
2026-09-09,XI,Laki-laki,13:00
2026-09-09,XII,Perempuan,09:30
2026-09-10,X,Perempuan,10:00
2026-09-10,XI,Laki-laki,12:30
2026-09-11,XII,Perempuan,13:00
2026-09-11,X,Laki-laki,14:00
2026-09-12,XI,Perempuan,09:00
2026-09-12,XII,Laki-laki,10:00
```

**Catatan:** Dataset merupakan data simulasi, bukan catatan kunjungan aktual perpustakaan. Atribut waktu tersedia dalam dataset, tetapi versi program saat ini belum menggunakan waktu untuk analisis khusus.

## Alur Kerja Program

1. Membaca dataset kunjungan dari `dataset.csv`.
2. Mengubah kolom tanggal menjadi format datetime.
3. Membersihkan spasi berlebih pada data kelas dan gender.
4. Menyediakan filter berdasarkan kelas dan gender.
5. Menghitung ringkasan jumlah kunjungan berdasarkan data hasil filter.
6. Mengelompokkan data berdasarkan tanggal untuk membuat grafik tren.
7. Menghitung jumlah kunjungan berdasarkan kelas.
8. Menghitung proporsi kunjungan berdasarkan gender.
9. Menampilkan tabel data kunjungan.
10. Menyediakan fitur unduh data hasil filter dalam format CSV.

## Struktur Folder

```text
Dashboard-Visualisasi-Data/
├── .venv/
├── main.py
├── dataset.csv
├── requirements.txt
├── README.md
└── .gitignore
```

Keterangan:

- `.venv/`: lingkungan Python terpisah untuk proyek.
- `main.py`: kode utama dashboard Streamlit.
- `dataset.csv`: dataset simulasi kunjungan perpustakaan.
- `requirements.txt`: daftar library yang dibutuhkan.
- `README.md`: dokumentasi proyek.
- `.gitignore`: daftar file dan folder yang tidak perlu diunggah ke GitHub.

## Penerapan Materi Webinar

Proyek ini menerapkan beberapa konsep Human-Computer Interaction dan Data Visualization.

### 1. User-Centered Design (UCD)

Dashboard menyajikan ringkasan utama dan filter agar pengguna dapat menemukan informasi yang dibutuhkan dengan lebih mudah.

### 2. Cognitive Load Theory

Informasi disajikan melalui metrik, grafik, dan tabel untuk membantu pengguna memahami data tanpa harus membaca seluruh data mentah satu per satu.

### 3. Recognition over Recall

Pilihan filter dan label grafik membantu pengguna mengenali kategori data yang tersedia tanpa harus mengingatnya secara manual.

### 4. Data Visualization

Pemilihan grafik disesuaikan dengan tujuan analisis:

- **Line Chart:** melihat tren kunjungan harian.
- **Bar Chart:** membandingkan jumlah kunjungan berdasarkan kelas.
- **Donut Chart:** melihat proporsi kunjungan berdasarkan gender.

### 5. Ethical Design

Dataset dijelaskan sebagai data simulasi sehingga hasil visualisasi tidak disalahartikan sebagai kondisi kunjungan perpustakaan yang sebenarnya.

## Batasan Proyek

- Dataset masih berupa data simulasi dengan jumlah terbatas.
- Dashboard belum terhubung dengan sistem pencatatan kunjungan secara langsung.
- Analisis waktu kunjungan belum dikembangkan.
- Hasil visualisasi hanya mencerminkan data yang tersedia dan filter yang dipilih.
- Dashboard belum memiliki autentikasi pengguna maupun penyimpanan data baru.

## Kesimpulan

Proyek ini mengembangkan dashboard visualisasi data pengunjung perpustakaan menggunakan Streamlit, Pandas, dan Plotly. Dashboard menyediakan ringkasan kunjungan, tren harian, perbandingan berdasarkan kelas, proporsi gender, filter interaktif, tabel data, dan fitur unduh CSV.

Penerapan prinsip HCI, UCD, dan Data Visualization diharapkan dapat membantu pengguna memahami informasi dengan lebih mudah. Proyek ini juga menjadi dasar pengembangan sistem analisis kunjungan perpustakaan yang lebih interaktif dan berbasis data.