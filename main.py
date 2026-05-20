import json
import os
from models import Pendaftar, UKM, seleksi

# ================= KONFIGURASI & TEMPLATE =================
FILE_DATA = "data_ormawa.json"

# Daftar UKM Standar yang harus selalu ada
UKM_AWAL = [
    {"nama": "UKM Robotika", "desk": "Fokus pengembangan robot dan AI", "kuota": 5},
    {"nama": "UKM Paduan Suara", "desk": "Pengembangan bakat seni suara", "kuota": 10},
    {"nama": "UKM Olahraga", "desk": "Fokus pada pengembangan fisik dan kerjasama tim", "kuota": 15},
    {"nama": "UKM Mapala", "desk": "Kegiatan alam bebas dan pelestarian lingkungan", "kuota": 10}
]

# ================= FUNGSI PENYIMPANAN =================
def simpan_data(list_ukm, list_pendaftar):
    data = {
        "ukm": [ukm.to_dict() for ukm in list_ukm],
        "pendaftar": [p.to_dict() for p in list_pendaftar]
    }
    with open(FILE_DATA, "w") as f:
        json.dump(data, f, indent=4)

def muat_data():
    list_ukm = []
    list_pendaftar = []
    
    # 1. Baca data lama jika ada
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r") as f:
                data = json.load(f)
                for u_data in data.get("ukm", []):
                    list_ukm.append(UKM.from_dict(u_data))
                for p_data in data.get("pendaftar", []):
                    list_pendaftar.append(Pendaftar.from_dict(p_data))
        except (json.JSONDecodeError, FileNotFoundError):
            pass

    # 2. LOGIKA MERGE: Tambahkan UKM template jika belum ada di list
    # Ini memastikan data tidak teriset, hanya bertambah
    nama_ukm_terdaftar = [u.nama_ukm for u in list_ukm]
    perlu_simpan = False
    
    for template in UKM_AWAL:
        if template["nama"] not in nama_ukm_terdaftar:
            list_ukm.append(UKM(template["nama"], template["desk"], template["kuota"]))
            perlu_simpan = True
            
    # Jika baru pertama kali (file belum ada) atau ada UKM baru ditambahkan, simpan ke file
    if perlu_simpan or not os.path.exists(FILE_DATA):
        simpan_data(list_ukm, list_pendaftar)
        
    return list_ukm, list_pendaftar

# Muat data saat program pertama kali berjalan
list_ukm, list_pendaftar = muat_data()

while True:
    print("\n" + "="*35)
    print("  SISTEM PENDAFTARAN ORMAWA FST  ")
    print("="*35)
    print("1. Masuk sebagai User / Pendaftar")
    print("2. Masuk sebagai Admin")
    print("0. Keluar Aplikasi")
    print("="*35)
    
    pilihan_login = input("Pilih angka untuk peran Anda: ")
    
    if pilihan_login == "1":
        # ================= MENU USER =================
        while True:
            print("\n" + "-"*30)
            print("   MENU USER / PENDAFTAR")
            print("-"*30)
            print("1. Pilih UKM & Isi Formulir")
            print("2. Lihat Status Pendaftaran")
            print("0. Kembali ke Menu Utama")
            print("-"*30)
            
            pilih_user = input("Pilih menu: ")
            
            if pilih_user == "1":
                print("\n--- Formulir: Pemilihan UKM ---")
                
                # 1. Menampilkan daftar UKM yang tersedia TERLEBIH DAHULU
                for i, ukm in enumerate(list_ukm):
                    print(f"{i+1}. {ukm.nama_ukm} (Kuota: {ukm.kuota_pendaftar})")
                
                try:
                    pilih_ukm = int(input("Pilih nomor UKM yang ingin diikuti: ")) - 1
                    
                    # Cek apakah pilihan UKM valid
                    if 0 <= pilih_ukm < len(list_ukm):
                        print(f"\nAnda memilih: {list_ukm[pilih_ukm].nama_ukm}")
                        print("--- Masukkan Data Diri ---")
                        
                        # 2. Mengambil input data Civitas & Pendaftar SETELAH memilih UKM
                        nama = input("Nama Lengkap    : ")
                        nim = input("NIM             : ")
                        prodi = input("Program Studi   : ")
                        fakultas = input("Fakultas        : ")
                        tgl_lahir = input("Tanggal Lahir  : ")
                        angkatan = input("Angkatan        : ")
                        kontak = input("Nomor Kontak    : ")
                        
                        riwayat = input("Riwayat Organisasi: ")
                        motivasi = input("Motivasi Memilih  : ")
                        
                        # 3. Membuat objek Pendaftar baru
                        mhs_baru = Pendaftar(
                            nama, nim, prodi, fakultas, tgl_lahir, angkatan, kontak,
                            riwayat_organisasi=riwayat, status_kelulusan="Diproses", motivasi=motivasi
                        )
                        
                        # 4. Memasukkan pendaftar ke list global dan list internal milik UKM
                        list_pendaftar.append(mhs_baru)
                        list_ukm[pilih_ukm].tambah_pendaftar(mhs_baru) 
                        
                        # 5. SIMPAN DATA KE FILE JSON
                        simpan_data(list_ukm, list_pendaftar)
                        print("\nPendaftaran berhasil dan data telah disimpan!")
                    else:
                        print("Pilihan UKM tidak valid. Pendaftaran dibatalkan.")
                        
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka.")
                    
            elif pilih_user == "2":
                print("\n--- Cek Status Kelulusan ---")
                cari_nim = input("Masukkan NIM Anda: ")
                ketemu = False
                for pendaftar in list_pendaftar:
                    if pendaftar.get_nim() == cari_nim:
                        print(f"Nama   : {pendaftar.nama}")
                        print(f"Status : {pendaftar.get_status_kelulusan()}")
                        ketemu = True
                        break
                if not ketemu:
                    print("Data pendaftar dengan NIM tersebut tidak ditemukan.")
                    
            elif pilih_user == "0":
                break
            else:
                print("Pilihan tidak valid!")

    elif pilihan_login == "2":
        # ================= MENU ADMIN =================
        while True:
            print("\n" + "#"*30)
            print("   MENU ADMIN UTAMA")
            print("#"*30)
            print("1. Kelola Data UKM")
            print("2. Kelola Data Pendaftar & Seleksi")
            print("0. Kembali ke Menu Utama")
            print("#"*30)
            
            pilih_admin = input("Pilih menu admin: ")
            
            if pilih_admin == "1":
                # Sub-menu Kelola UKM
                print("\n--- Kelola Data UKM ---")
                print("1. Tambah UKM Baru")
                print("2. Lihat Daftar UKM")
                sub_ukm = input("Pilih: ")
                
                if sub_ukm == "1":
                    nama_ukm = input("Nama UKM baru     : ")
                    desk = input("Deskripsi Kegiatan: ")
                    kuota = int(input("Kuota Pendaftar   : "))
                    
                    ukm_baru = UKM(nama_ukm, desk, kuota)
                    list_ukm.append(ukm_baru)
                    print(f"UKM {nama_ukm} berhasil didaftarkan ke sistem.")
                    
                elif sub_ukm == "2":
                    print("\n--- Daftar Seluruh UKM ---")
                    for ukm in list_ukm:
                        print(f"- {ukm.nama_ukm} | {ukm.desk_kegiatan} (Kuota: {ukm.kuota_pendaftar})")
                        
            elif pilih_admin == "2":
                print("\n--- Kelola Pendaftar & Input Nilai ---")
                if not list_pendaftar:
                    print("Belum ada mahasiswa yang mendaftar.")
                    continue
                    
                for i, p in enumerate(list_pendaftar):
                    # Tampilkan nilai rata-rata jika sudah dinilai
                    info_nilai = f"- Rata-rata: {p.hasil_seleksi.hitung_rata_rata():.2f}" if p.hasil_seleksi else "- Belum dinilai"
                    print(f"{i+1}. {p.nama} (NIM: {p.get_nim()}) | Status: {p.get_status_kelulusan()} {info_nilai}")
                    
                try:
                    pilih_mhs = int(input("\nPilih nomor mahasiswa untuk dinilai (atau 0 untuk batal): ")) - 1
                    
                    if pilih_mhs == -1:
                        continue
                    elif 0 <= pilih_mhs < len(list_pendaftar):
                        mhs = list_pendaftar[pilih_mhs]
                        
                        print(f"\nInput Nilai Seleksi untuk {mhs.nama}:")
                        n_wawancara = int(input("Nilai Wawancara (0-100)   : "))
                        n_terampil = int(input("Nilai Keterampilan (0-100): "))
                        n_sikap = int(input("Nilai Sikap (0-100)       : "))
                        
                        # 1. Membuat objek dari class seleksi
                        nilai_baru = seleksi(n_wawancara, n_terampil, n_sikap)
                        
                        # 2. Menempelkan objek seleksi ke mahasiswa (Agregasi)
                        mhs.hasil_seleksi = nilai_baru
                        
                        # 3. Panggil method di class seleksi untuk menghitung rata-rata
                        nilai_akhir = mhs.hasil_seleksi.hitung_rata_rata()
                        
                        # 4. Tentukan Kelulusan
                        if nilai_akhir >= 70:
                            mhs.set_status_kelulusan("LULUS")
                            print(f"Hasil: {mhs.nama} dinyatakan LULUS dengan rata-rata {nilai_akhir:.2f}")
                        else:
                            mhs.set_status_kelulusan("TIDAK LULUS")
                            print(f"Hasil: {mhs.nama} dinyatakan TIDAK LULUS dengan rata-rata {nilai_akhir:.2f}")
                            
                        # 5. SIMPAN DATA KE FILE JSON AGAR NILAI TIDAK HILANG
                        simpan_data(list_ukm, list_pendaftar)
                        
                    else:
                        print("Pilihan tidak valid.")
                except ValueError:
                    print("Input tidak valid! Masukkan angka.")
                    
            elif pilih_admin == "0":
                break
            else:
                print("Pilihan tidak valid!")
                
    elif pilihan_login == "0":
        print("\nTerima kasih telah menggunakan sistem ini. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid! Masukkan angka 1, 2, atau 0.")