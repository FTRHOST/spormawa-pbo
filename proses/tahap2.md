# Tahap 2: Implementasi Enkapsulasi dan Pewarisan

Pada tahap ini, struktur class yang telah dirancang pada Tahap 1 diimplementasikan dengan prinsip Pemrograman Berorientasi Objek (OOP) yang lebih mendalam, yaitu Pewarisan (Inheritance) dan Enkapsulasi (Encapsulation).

## 1. Pewarisan (Inheritance)
Kelas `Pendaftar` mewarisi sifat dan atribut dari kelas `Civitas`. Hal ini memungkinkan `Pendaftar` memiliki atribut dasar seperti `nama`, `NIM`, `prodi`, dll., tanpa harus mendefinisikannya ulang.

### Penggunaan `super()`
Fungsi `super()` digunakan di dalam constructor `Pendaftar` untuk memanggil constructor dari parent class (`Civitas`), sehingga inisialisasi atribut dasar dapat dilakukan dengan efisien.

```python
class Pendaftar(Civitas):
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak, riwayat_organisasi, status_kelulusan, motivasi, ukm_pilihan="Belum Memilih"):
        # Memanggil constructor parent class
        super().__init__(nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak)
        self.riwayat_organisasi = riwayat_organisasi
        self.__status_kelulusan = status_kelulusan
        self.motivasi = motivasi
        self.ukm_pilihan = ukm_pilihan
        self.hasil_seleksi = None
```

## 2. Enkapsulasi (Encapsulation)
Data sensitif diamankan menggunakan akses private (dengan awalan double underscore `__`). Hal ini mencegah akses langsung dari luar class dan memastikan integritas data.

### Atribut Private
- `Civitas.__NIM`: Mengamankan Nomor Induk Mahasiswa.
- `Pendaftar.__status_kelulusan`: Mengamankan status kelulusan agar hanya bisa diubah melalui mekanisme seleksi yang sah.

### Getter dan Setter
Untuk mengakses dan mengubah atribut private, digunakan metode Getter dan Setter.

```python
# Di dalam class Civitas
def get_nim(self):
    return self.__NIM

# Di dalam class Pendaftar
def get_status_kelulusan(self):
    return self.__status_kelulusan

def set_status_kelulusan(self, status):
    self.__status_kelulusan = status
```

## 3. Verifikasi Objek (Terminal)
Objek dapat diinstansiasi secara manual melalui terminal Python untuk memastikan logika inheritance dan enkapsulasi berjalan dengan baik.

### Contoh Instansiasi
```python
from models import Pendaftar

# Membuat objek pendaftar baru
mhs = Pendaftar(
    "Budi Santoso", 
    2200101, 
    "Informatika", 
    "Sains dan Teknologi", 
    "2004-05-10", 
    2022, 
    "08123456789", 
    "OSIS SMA 1", 
    "Diproses", 
    "Ingin belajar robotika"
)

# Menampilkan data menggunakan getter
print(f"Nama: {mhs.nama}")
print(f"NIM (via getter): {mhs.get_nim()}")
print(f"Status: {mhs.get_status_kelulusan()}")

# Mengubah status menggunakan setter
mhs.set_status_kelulusan("LULUS")
print(f"Status Terbaru: {mhs.get_status_kelulusan()}")
```

## Kesimpulan Tahap 2
- Kelas telah terhubung melalui **Inheritance**.
- Atribut sensitif telah dilindungi dengan **Encapsulation**.
- Akses data dilakukan secara aman melalui **Getter/Setter**.
- Objek siap untuk dilanjutkan ke tahap berikutnya (Polimorfisme dan Abstraksi).
