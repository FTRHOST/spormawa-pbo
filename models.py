class Civitas:
    def __init__(self, nama, NIM, prodi, fakultas, tanggal_lahir, angkatan, kontak):
        self.nama = nama
        self.NIM = NIM
        self.prodi = prodi
        self.fakultas = fakultas
        self.tanggal_lahir = tanggal_lahir
        self.angkatan = angkatan
        self.kontak = kontak
        pass

class Pendaftar:
    def __init__(self, riwayat_organisasi, status_kelulusan, motivasi):
        self.riwayat_organisasi = riwayat_organisasi
        self.__status_kelulusan = status_kelulusan       
        self.motivasi = motivasi
        pass
    
class UKM:
    def __init__(self, nama_ukm, desk_kegiatan, kuota_pendaftar):
        self.nama_ukm = nama_ukm
        self.desk_kegiatan = desk_kegiatan
        self.kuota_pendaftar = kuota_pendaftar
        pass

class seleksi:
    def __init__(self, nilai_wawancara, nilai_keterampilan, nilai_sikap):
        self.nilai_wawancara = nilai_wawancara
        self.nilai_keterampilan = nilai_keterampilan
        self.nilai_sikap = nilai_sikap
        pass
       
