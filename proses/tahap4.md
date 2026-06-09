# Tahap 4: Pembuatan Menu Interaktif (CLI)

Tahap ini berfokus pada pembangunan antarmuka pengguna berbasis teks (Command Line Interface) yang memungkinkan interaksi dinamis antara pengguna dan sistem.

## 1. Struktur Perulangan Utama
Sistem menggunakan struktur `while True` untuk menjaga program tetap berjalan hingga pengguna memilih untuk keluar. Terdapat dua level menu: Menu Utama (Login) dan Menu Peran (User/Admin).

```python
while True:
    print("1. Masuk sebagai User")
    print("2. Masuk sebagai Admin")
    print("0. Keluar")
    
    pilihan = input("Pilih peran: ")
    if pilihan == "0":
        break # Keluar dari program
```

## 2. Menu Interaktif Peran
Setiap peran memiliki menu spesifik yang dikelola dalam perulangan bersarang (*nested loop*).

### Menu User
- **Pilih UKM & Isi Formulir:** Mengambil input data diri.
- **Lihat Status:** Mengecek hasil seleksi berdasarkan NIM.

### Menu Admin
- **Kelola Data UKM:** Menambah atau melihat daftar UKM.
- **Kelola Pendaftar & Seleksi:** Melakukan penilaian terhadap mahasiswa yang mendaftar.

## 3. Konversi Input ke Objek
Setiap data yang dimasukkan melalui fungsi `input()` diproses dan langsung diinstansiasi menjadi objek dari class yang sesuai.

### Contoh Pembuatan Objek Pendaftar:
Saat user mengisi formulir, data ditampung dalam variabel dan dikonversi menjadi objek `Pendaftar`:
```python
# Mengambil input
nama = input("Nama Lengkap: ")
nim = input("NIM: ")
# ... input lainnya ...

# Instansiasi Objek
mhs_baru = Pendaftar(nama, nim, prodi, fakultas, tgl_lahir, angkatan, kontak, riwayat, "Diproses", motivasi, ukm_pilihan)

# Menyimpan ke dalam list
list_pendaftar.append(mhs_baru)
```

## 4. Validasi Input
Untuk menjaga stabilitas program, digunakan blok `try-except` pada input yang bersifat numerik (seperti pemilihan menu atau input nilai) untuk mencegah program berhenti tiba-tiba (*crash*) jika user memasukkan karakter non-angka.

```python
try:
    pilih_menu = int(input("Pilih nomor: "))
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
```

## Kesimpulan Tahap 4
- Antarmuka telah bersifat **interaktif** dan mendukung navigasi menu.
- Sistem mampu mengubah **data mentah (input)** menjadi **entitas data (Object)** yang terstruktur.
- Pemisahan peran antara **User** dan **Admin** sudah terimplementasi dengan baik dalam logika program.
