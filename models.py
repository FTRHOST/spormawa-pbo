class Civitas:
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak):
        self.nama = nama
        self.__NIM = NIM
        self.prodi = prodi
        self.fakultas = fakultas
        self.tanggal_lahir = tanggal_lahir
        self.angkatan = angkatan
        self.kontak = kontak

    def get_nim(self):
        return self.__NIM

    # Method untuk mengubah data Civitas menjadi dictionary (dipakai saat save)
    def to_dict(self):
        return {
            "nama": self.nama,
            "NIM": self.get_nim(),
            "prodi": self.prodi,
            "fakultas": self.fakultas,
            "tanggal_lahir": self.tanggal_lahir,
            "angkatan": self.angkatan,
            "kontak": self.kontak
        }

class Pendaftar(Civitas):
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak, riwayat_organisasi, status_kelulusan, motivasi):
        super().__init__(nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak)
        self.riwayat_organisasi = riwayat_organisasi
        self.__status_kelulusan = status_kelulusan
        self.motivasi = motivasi
        self.hasil_seleksi = None  # <--- TAMBAHKAN INI (Nilai awal kosong sebelum dinilai Admin)

    def get_status_kelulusan(self):
        return self.__status_kelulusan

    def set_status_kelulusan(self, status):
        self.__status_kelulusan = status

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "riwayat_organisasi": self.riwayat_organisasi,
            "status_kelulusan": self.get_status_kelulusan(),
            "motivasi": self.motivasi,
            # Simpan data seleksi jika admin sudah memberi nilai
            "hasil_seleksi": self.hasil_seleksi.to_dict() if self.hasil_seleksi else None
        })
        return data

    @classmethod
    def from_dict(cls, data):
        # Buat objek pendaftar
        pendaftar = cls(
            data["nama"], data["NIM"], data["prodi"], data["fakultas"],
            data["tanggal_lahir"], data["angkatan"], data["kontak"],
            data["riwayat_organisasi"], data["status_kelulusan"], data["motivasi"]
        )
        # Jika di JSON ada data "hasil_seleksi", ubah kembali jadi objek Seleksi
        if data.get("hasil_seleksi"):
            pendaftar.hasil_seleksi = seleksi.from_dict(data["hasil_seleksi"])
            
        return pendaftar
    
class UKM:
    def __init__(self, nama_ukm, desk_kegiatan, kuota_pendaftar):
        self.nama_ukm = nama_ukm
        self.desk_kegiatan = desk_kegiatan
        self.kuota_pendaftar = kuota_pendaftar
        self.daftar_pendaftar = []

    def tambah_pendaftar(self, pendaftar):
        if len(self.daftar_pendaftar) < self.kuota_pendaftar:
            self.daftar_pendaftar.append(pendaftar)
        else:
            print("Kuota pendaftar penuh!")

    def to_dict(self):
        return {
            "nama_ukm": self.nama_ukm,
            "desk_kegiatan": self.desk_kegiatan,
            "kuota_pendaftar": self.kuota_pendaftar
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nama_ukm"], data["desk_kegiatan"], data["kuota_pendaftar"])

class seleksi:
    def __init__(self, nilai_wawancara, nilai_keterampilan, nilai_sikap):
        self.nilai_wawancara = nilai_wawancara
        self.nilai_keterampilan = nilai_keterampilan
        self.nilai_sikap = nilai_sikap
        
    # Fungsi logika bisnis untuk menghitung rata-rata
    def hitung_rata_rata(self):
        return (self.nilai_wawancara + self.nilai_keterampilan + self.nilai_sikap) / 3

    # Method untuk mengubah objek seleksi jadi dictionary (untuk disave)
    def to_dict(self):
        return {
            "nilai_wawancara": self.nilai_wawancara,
            "nilai_keterampilan": self.nilai_keterampilan,
            "nilai_sikap": self.nilai_sikap
        }

    @classmethod
    def from_dict(cls, data):
        # Jika belum ada data seleksi, kembalikan None
        if not data:
            return None
        return cls(data["nilai_wawancara"], data["nilai_keterampilan"], data["nilai_sikap"])