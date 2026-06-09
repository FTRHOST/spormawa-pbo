```markdown
# Tahap 2: Implementasi Enkapsulasi dan Pewarisan

Pada tahap ini, arsitektur *class* yang telah dirancang pada Tahap 1 dihubungkan menggunakan konsep *Inheritance* (Pewarisan) dan data di dalamnya diamankan menggunakan *Encapsulation* (Enkapsulasi).

## 1. Inheritance (Pewarisan)
Sistem menerapkan hierarki pewarisan di mana class `Civitas` bertindak sebagai *Superclass* (Induk) dan class `Pendaftar` bertindak sebagai *Subclass* (Turunan).
* Class `Pendaftar` mewarisi seluruh atribut dasar dari `Civitas` (seperti nama, prodi, fakultas, tanggal_lahir, angkatan, dan kontak).
* Pemanggilan konstruktor dari *class* induk dilakukan menggunakan fungsi `super().__init__()` untuk menghindari duplikasi inisialisasi kode.

```python
# Implementasi pada class Pendaftar di models.py
class Pendaftar(Civitas):
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak, riwayat_organisasi, status_kelulusan, motivasi, ukm_pilihan="Belum Memilih"):
        # Memanggil konstruktor superclass Civitas
        super().__init__(nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak)
        
        # Atribut spesifik milik subclass Pendaftar
        self.riwayat_organisasi = riwayat_organisasi
        self.__status_kelulusan = status_kelulusan
        self.motivasi = motivasi
        self.ukm_pilihan = ukm_pilihan 
        self.hasil_seleksi = None

```

## 2. Encapsulation (Enkapsulasi)

Atribut-atribut yang bersifat krusial dilindungi menggunakan *Private Modifier* (`__`) agar nilainya tidak dapat dimodifikasi atau diakses secara sembarangan dari luar *class*. Akses ke data tersebut dijembatani melalui metode *Getter* dan *Setter*.

### A. Enkapsulasi pada Class `Civitas`

Atribut `NIM` diamankan menjadi *private* (`__NIM`) dan hanya bisa dibaca menggunakan metode `get_nim()`.

```python
class Civitas:
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak):
        self.nama = nama
        self.__NIM = NIM  # Diatur sebagai atribut private
        self.prodi = prodi
        # ... atribut lainnya ...

    # Getter untuk mengakses NIM
    def get_nim(self):
        return self.__NIM

```

### B. Enkapsulasi pada Class `Pendaftar`

Atribut `status_kelulusan` diamankan menjadi *private* (`__status_kelulusan`) untuk mencegah perubahan status pendaftaran secara langsung (ilegal) tanpa melalui logika program/admin. Akses dan modifikasinya wajib menggunakan `get_status_kelulusan()` dan `set_status_kelulusan()`.

```python
class Pendaftar(Civitas):
    # ... (bagian init) ...

    # Getter untuk melihat status
    def get_status_kelulusan(self):
        return self.__status_kelulusan

    # Setter untuk mengubah status (misalnya saat admin memberikan penilaian)
    def set_status_kelulusan(self, status):
        self.__status_kelulusan = status

```

## 3. Pengujian Instansiasi Objek

Dengan implementasi di atas, objek pengguna sudah dapat diinstansiasi dengan baik. Atribut private seperti `__NIM` dan `__status_kelulusan` kini tidak akan muncul jika diakses langsung (misal: `print(mhs.__NIM)` akan menghasilkan *error*), melainkan harus dipanggil via `mhs.get_nim()`.

```

```
