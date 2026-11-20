
class Mahasiswa:
    # Constructor
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.__nilai = 0
        self.nilai = nilai

    # Property (Getter)
    @property
    def nilai(self):
        return self.__nilai

    # Setter
    @nilai.setter
    def nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            print("Nilai harus antara 0-100!")

    # Method
    def tampilkan_data(self):
        print("Nama  :", self.nama)
        print("NIM   :", self.nim)
        print("Nilai :", self.nilai)
        print("Status:", self.status_kelulusan())

    # Method
    def status_kelulusan(self):
        if self.nilai >= 60:
            return "Lulus"
        else:
            return "Tidak Lulus"

    # Static Method
    @staticmethod
    def informasi():
        return "Program Sistem Data Mahasiswa"


class SistemMahasiswa:
    # Class Attribute
    jumlah_mahasiswa = 0

    # Constructor
    def __init__(self):
        self.daftar_mahasiswa = []

    # Method menambahkan mahasiswa
    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        SistemMahasiswa.jumlah_mahasiswa += 1
        print("Data mahasiswa berhasil ditambahkan!")

    # Method menampilkan semua mahasiswa
    def tampilkan_semua(self):
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        for mahasiswa in self.daftar_mahasiswa:
            print("----------------------")
            mahasiswa.tampilkan_data()

    # Class Method
    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa


# Membuat object
sistem = SistemMahasiswa()

# Menu program
while True:
    print("\n===== SISTEM DATA MAHASISWA =====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Total Mahasiswa")
    print("4. Informasi Program")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")

        try:
            nilai = float(input("Masukkan Nilai: "))

            mahasiswa = Mahasiswa(nama, nim, nilai)
            sistem.tambah_mahasiswa(mahasiswa)

        except ValueError:
            print("Nilai harus berupa angka!")

    elif pilihan == "2":
        sistem.tampilkan_semua()

    elif pilihan == "3":
        print("Total Mahasiswa:",
              SistemMahasiswa.total_mahasiswa())

    elif pilihan == "4":
        print(Mahasiswa.informasi())

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid!")
