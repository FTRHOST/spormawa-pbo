# Tahap 3: Implementasi Polimorfisme dan Logika Bisnis

Tahap ini berfokus pada penerapan logika inti sistem dan penggunaan Polimorfisme untuk menangani objek dari berbagai class dengan cara yang seragam namun memiliki perilaku spesifik.

## 1. Polimorfisme (Method Overriding)
Polimorfisme diimplementasikan melalui *method overriding*, di mana class anak (`Pendaftar`) memberikan implementasi spesifik untuk method yang sudah didefinisikan di class induk (`Civitas`).

### Method `tampilkan_info()`
Method ini didefinisikan di `Civitas` untuk menampilkan data dasar, namun di-override di `Pendaftar` untuk menampilkan status pendaftaran.

```python
# Di dalam class Civitas
def tampilkan_info(self):
    print(f"[Civitas] Nama: {self.nama} | NIM: {self.get_nim()}")

# Di dalam class Pendaftar (Override)
def tampilkan_info(self):
    print(f"[Pendaftar] Nama: {self.nama} | UKM Pilihan: {self.ukm_pilihan} | Status: {self.get_status_kelulusan()}")
```

### Keuntungan Polimorfisme
Dengan polimorfisme, kita bisa memproses daftar objek `Civitas` dan `Pendaftar` dalam satu loop yang sama tanpa perlu mengecek tipe class-nya secara manual:
```python
list_orang = [civitas_obj, pendaftar_obj]
for orang in list_orang:
    orang.tampilkan_info() # Akan memanggil method yang sesuai secara otomatis
```

## 2. Logika Bisnis (Core Process)
Logika bisnis utama dalam sistem ini mencakup perhitungan nilai seleksi dan manajemen kuota UKM.

### Perhitungan Nilai Seleksi
Class `seleksi` bertanggung jawab menghitung rata-rata nilai dari tiga komponen (wawancara, keterampilan, sikap).
```python
def hitung_rata_rata(self):
    return (self.nilai_wawancara + self.nilai_keterampilan + self.nilai_sikap) / 3
```

### Validasi Kuota UKM
Class `UKM` memiliki logika untuk memastikan pendaftar tidak melebihi kuota yang tersedia.
```python
def tambah_pendaftar(self, pendaftar):
    if len(self.daftar_pendaftar) < self.kuota_pendaftar:
        self.daftar_pendaftar.append(pendaftar)
    else:
        print("Kuota pendaftar penuh!")
```

## 3. Verifikasi Logika Bisnis
Logika kelulusan di dalam `main.py` menggunakan hasil dari class `seleksi` untuk menentukan status akhir pendaftar.

### Alur Seleksi:
1. Admin menginput nilai (0-100).
2. Sistem menghitung rata-rata menggunakan `hitung_rata_rata()`.
3. Jika rata-rata >= 70, status diubah menjadi **LULUS** menggunakan setter `set_status_kelulusan()`.

## Kesimpulan Tahap 3
- **Polimorfisme** memungkinkan fleksibilitas dalam menampilkan informasi objek.
- **Logika Bisnis** telah terisolasi di dalam class masing-masing (Encapsulation of Logic).
- Sistem sudah dapat menjalankan fungsi utamanya: **Pendaftaran -> Seleksi -> Penentuan Kelulusan**.
