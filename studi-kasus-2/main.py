import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "cuaca.csv"

def tentukan_risiko(curah_hujan):
    # Batas kategori ini hanya contoh pembelajaran.
    if curah_hujan >= 100:
        return "Tinggi"
    elif curah_hujan >= 50:
        return "Sedang"
    return "Rendah"

def main():
    data = pd.read_csv(DATA_PATH)
    data["curah_hujan_mm"] = pd.to_numeric(data["curah_hujan_mm"], errors="coerce")
    data = data.dropna(subset=["curah_hujan_mm"])

    if data.empty:
        print("Data curah hujan tidak tersedia.")
        return

    data["risiko"] = data["curah_hujan_mm"].apply(tentukan_risiko)

    print("=== ANALISIS DATA CUACA SEDERHANA ===")
    print(data.to_string(index=False))
    print(f"\nRata-rata curah hujan: {data['curah_hujan_mm'].mean():.1f} mm")
    print(f"Curah hujan tertinggi: {data['curah_hujan_mm'].max():.1f} mm")

    tinggi = data[data["risiko"] == "Tinggi"]
    print(f"Jumlah hari dengan kategori risiko tinggi: {len(tinggi)}")
    if not tinggi.empty:
        print("\nHari yang perlu diperhatikan:")
        print(tinggi[["tanggal", "wilayah", "curah_hujan_mm"]].to_string(index=False))

    print("\nCatatan: kategori ini hanya contoh pembelajaran, bukan peringatan resmi.")

if __name__ == "__main__":
    main()
