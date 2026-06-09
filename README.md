# SPORMAWA-PBO (Sistem Pendaftaran Ormawa)

Sistem Pendaftaran Organisasi Mahasiswa (ORMAWA) berbasis Python CLI yang dirancang dengan prinsip Pemrograman Berorientasi Objek (OOP). Sistem ini memungkinkan mahasiswa untuk mendaftar ke berbagai UKM dan memungkinkan Admin untuk melakukan seleksi nilai serta menentukan kelulusan.

oleh:
1. 43050250031 ANDI KURNIAWAN
2. 43050250010 MIFTAKHUL ANWAR
3. 43050250011 MUHAMMAD FATHIR AL FARUQ
4. 43050250034 RIZKY ANGFAUZY

## Fitur Utama
- **Role User:** Memilih UKM, mengisi formulir pendaftaran, dan mengecek status kelulusan.
- **Role Admin:** Mengelola data UKM (tambah/lihat) dan memberikan penilaian seleksi kepada pendaftar.
- **Persistence:** Data disimpan secara otomatis dalam format JSON (`data_ormawa.json`).
- **OOP Principles:** Menerapkan Inheritance, Encapsulation, Polymorphism, dan Abstraction.

## Dokumentasi Proses Pengembangan
Berikut adalah rincian tahapan pengembangan proyek ini:

1.  **[Tahap 1: Perancangan Arsitektur dan Draft Class](proses/tahap1.md)**
    *   Perancangan struktur kelas dan diagram alir (Mermaid).
2.  **[Tahap 2: Implementasi Enkapsulasi dan Pewarisan](proses/tahap2.md)**
    *   Penghubungan kelas dengan Inheritance dan pengamanan data dengan Private Attributes & Getter/Setter.
3.  **[Tahap 3: Implementasi Polimorfisme dan Logika Bisnis](proses/tahap3.md)**
    *   Penerapan method overriding dan logika inti perhitungan seleksi serta kuota.
4.  **[Tahap 4: Pembuatan Menu Interaktif (CLI)](proses/tahap4.md)**
    *   Pembangunan antarmuka berbasis teks dengan perulangan `while True` dan input interaktif.

## Cara Menjalankan
1. Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Jalankan perintah berikut di terminal:
   ```bash
   python main.py
   ```

## Struktur File
- `main.py`: Entry point aplikasi dan logika menu CLI.
- `models.py`: Definisi class (Civitas, Pendaftar, UKM, Seleksi).
- `proses/`: Folder berisi dokumentasi setiap tahap pengembangan.
- `data_ormawa.json`: File database lokal (dibuat otomatis).

---
*Proyek ini dikembangkan untuk memenuhi tugas mata kuliah Pemrograman Berorientasi Objek (PBO).*
