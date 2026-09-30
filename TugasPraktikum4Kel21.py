# ==========================================
# WATERMARK: KELOMPOK 21
# SISTEM MANAJEMEN INVENTARIS TOKO RITEL
# ==========================================

# 1. CLASS & METHOD (Konsep Object-Oriented untuk memenuhi syarat Method)
class InventarisToko:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        # Data awal produk: [Nama, Stok, Harga]
        self.produk_list = [
            ["Kemeja Alisan", 15, 150000],
            ["Celana Chino", 8, 200000],
            ["Jaket Parka", 5, 250000]
        ]

    # [METHOD 1] Non-Return Type (Tanpa Parameter)
    # Menampilkan seluruh data inventaris toko
    def tampilkan_stok(self):
        print(f"\n=== DAFTAR STOK PRODUK - {self.nama_toko.upper()} ===")
        print(f"{'No':<5}{'Nama Produk':<20}{'Stok':<10}{'Harga':<15}")
        print("-" * 50)
        
        # PERULANGAN: Menggunakan for loop untuk iterasi list
        for indeks, item in enumerate(self.produk_list, start=1):
            print(f"{indeks:<5}{item[0]:<20}{item[1]:<10}Rp {item[2]:,}")
        print("-" * 50)

    # [METHOD 2] Non-Return Type (Berparameter)
    # Menambahkan produk baru ke dalam inventaris
    def tambah_produk(self, nama, stok, harga):
        self.produk_list.append([nama, stok, harga])
        print(f"\n[SUKSES] Produk '{nama}' berhasil ditambahkan ke inventaris Kelompok 21!")


# 2. FUNCTION (Fungsi Independen di luar Class)

# [FUNCTION 1] Return Type (Berparameter)
# Menghitung total nilai aset dari satu jenis produk (Stok x Harga)
def hitung_nilai_aset_produk(stok, harga):
    total = stok * harga
    return total # Mengembalikan nilai keuangan produk tersebut


# [FUNCTION 2] Return Type (Tanpa Parameter)
# Menampilkan menu utama dan meminta input dari user
def dapatkan_pilihan_menu():
    print("\nMENU UTAMA:")
    print("1. Lihat Semua Stok & Aset")
    print("2. Tambah Produk Baru")
    print("3. Cek Status Restock Produk")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    return pilihan # Mengembalikan pilihan user dalam bentuk string


# 3. PROGRAM UTAMA (MAIN LOOP)
if __name__ == "__main__":
    # Inisialisasi Objek Toko
    toko_kita = InventarisToko("Toko Retail Kelompok 21")
    
    print("==================================================")
    # PENGGUNAAN WATERMARK DI CONSOLE
    print("      PROGRAM INVENTARIS OLEH: KELOMPOK 21        ")
    print("==================================================")

    # PERULANGAN: Main loop menggunakan while
    while True:
         menu_terpilih = dapatkan_pilihan_menu()

         # PENGKONDISIAN: Memproses pilihan menu user
         if menu_terpilih == "1":
             # Memanggil Method Non-Return Type tanpa parameter
             toko_kita.tampilkan_stok()
             
             # Tambahan visualisasi pemanggilan Function Return Type berparameter
             print("\nAnalisis Total Nilai Aset per Produk:")
             for item in toko_kita.produk_list:
                 aset = hitung_nilai_aset_produk(item[1], item[2])
                 print(f"- {item[0]}: Total Aset = Rp {aset:,}")

         elif menu_terpilih == "2":
             print("\n--- INPUT PRODUK BARU ---")
             nama = input("Masukkan nama produk : ")
             stok = int(input("Masukkan jumlah stok  : "))
             harga = int(input("Masukkan harga satuan : "))
             
             # Memanggil Method Non-Return Type dengan parameter
             toko_kita.tambah_produk(nama, stok, harga)

         elif menu_terpilih == "3":
             print("\n--- STATUS RESTOCK PRODUK (Stok < 10) ---")
             # PENGKONDISIAN & PERULANGAN digabung untuk memfilter data
             butuh_restock = False
             for item in toko_kita.produk_list:
                 if item[1] < 10: # Pengkondisian jika stok kritis kurang dari 10
                     print(f"[PERINGATAN] Produk '{item[0]}' kritis! Sisa stok hanya {item[1]}.")
                     butuh_restock = True
             
             if not butuh_restock:
                 print("[AMAN] Semua stok produk masih mencukupi.")

         elif menu_terpilih == "4":
             print("\nTerima kasih! Program selesai. (Watermark: KELOMPOK 21)")
             break # Menghentikan perulangan while
             
         else:
             print("\n[ERROR] Pilihan menu tidak valid! Silakan masukkan angka 1-4.")
