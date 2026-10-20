# Studi Kasus HPC: Analisis Data Cuaca

## Deskripsi
Program Python sederhana untuk membaca data cuaca dari CSV, menghitung ringkasan curah hujan, dan mengelompokkan data ke kategori risiko rendah, sedang, atau tinggi.

## Tujuan
- Mempraktikkan pengolahan data dengan Python.
- Menunjukkan contoh analisis yang dapat dikembangkan untuk pemantauan cuaca.
- Memahami hubungan studi kasus dengan High-Performance Computing (HPC).

## Catatan
Data pada proyek ini adalah data contoh untuk pembelajaran, bukan data cuaca aktual atau alat peringatan resmi. Batas kategori hanya aturan demonstrasi.

## Persyaratan
Python 3.10 atau lebih baru dan pandas.

## Cara menjalankan
1. Buka terminal pada folder proyek.
2. Instal dependensi: `pip install -r requirements.txt`
3. Jalankan: `python main.py`

## Struktur folder
```text
studi-kasus-hpc-cuaca/
├── data/
│   └── cuaca.csv
├── main.py
├── README.md
└── requirements.txt
```

## Hubungan dengan HPC
Program ini dijalankan pada komputer biasa karena datanya kecil. Jika data berasal dari banyak sensor, wilayah, dan periode waktu, HPC dapat membantu menjalankan pemrosesan atau simulasi secara paralel sehingga analisis dapat dilakukan lebih cepat.

## Pengembangan selanjutnya
- Menggunakan data cuaca resmi dari sumber tepercaya.
- Menambahkan grafik curah hujan.
- Memproses data dari banyak wilayah.
- Mencoba pemrosesan paralel untuk mempelajari konsep HPC.
