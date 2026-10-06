import time
from datetime import datetime
from prettytable import PrettyTable

stok_darah = {
    "D01" : {"Nama" : "DIANA", "Golongan Darah" : "A", "Jumlah Kantong" : 2, "Tanggal" : "06-10-2026"},
    "D02" : {"Nama" : "AUREL", "Golongan Darah" : "B", "Jumlah Kantong" : 3, "Tanggal" : "07-10-2026"},
    "D03" : {"Nama" : "LILY" , "Golongan Darah" : "O", "Jumlah Kantong" : 2, "Tanggal" : "08-10-2026"},
    "D04" : {"Nama" : "TZUYU", "Golongan Darah" : "AB", "Jumlah Kantong": 1, "Tanggal" : "09-10-2026"}
}

data_akun = {
    "admin1" : {"password" : "123", "role" : "ADMIN"},
    "user1"  : {"password" : "456", "role" : "USER"}
}

def input_jumlah(pesan="Jumlah Kantong : "):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah > 0:
                return jumlah
            print("input tidak valid, jumlah kantong harus lebih dari 0.")
        except ValueError:
            print("input harus berupa angka bulat.")


def login():
    print()
    print("_________________________________________")
    print("         === SILAHKAN LOGIN ===         ")
    print("_________________________________________")

    while True:
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        if username in data_akun and data_akun[username]["password"] == password:
            role = data_akun[username]["role"]
            print(">>> LOGIN BERHASIL <<<")
            return username, role
        else:
            print(">>> LOGIN GAGAL <<<")
            print("username atau password salah, silakan coba lagi.")


def tampilkan_stok():
    print("___________________________________________________")
    print("             === DAFTAR STOK DARAH ===             ")
    print("___________________________________________________")

    if len(stok_darah) == 0:
        print("STOK DARAH SEDANG KOSONG.")
    else:
        table = PrettyTable()
        table.field_names = ["ID Pendonor", "Nama", "Golongan Darah", "Jumlah Kantong", "Tanggal"]

        for id_donor, isi in stok_darah.items():
            table.add_row([
                id_donor,
                isi["Nama"],
                isi["Golongan Darah"],
                isi["Jumlah Kantong"],
                isi["Tanggal"]
            ])

        print(table)


def tambah_stok():
    print("___________________________________________________")
    print("          === TAMBAH DATA DONOR BARU ===          ")
    print("___________________________________________________")

    while True:
        id_donor = input("Masukkan ID Pendonor : ").strip().upper()
        if id_donor == "":
            print("ID donor tidak boleh kosong.")
        elif id_donor in stok_darah:
            print("ID sudah digunakan, silakan gunakan ID lain.")
        else:
            break

    while True:
        nama = input("Nama Pendonor : ").strip().upper()
        if nama != "":
            break
        print("Nama pendonor tidak boleh kosong.")

    while True:
        gol_darah = input("Golongan Darah (A/B/AB/O) : ").strip().upper()
        if gol_darah in ("A", "B", "AB", "O"):
            break
        print("Golongan darah tidak valid. Pilih A, B, AB, atau O.")

    jumlah_kantong = input_jumlah("Jumlah Kantong Darah : ")
    tanggal = datetime.now().strftime("%d-%m-%Y")

    stok_darah[id_donor] = {
        "Nama": nama,
        "Golongan Darah": gol_darah,
        "Jumlah Kantong": jumlah_kantong,
        "Tanggal": tanggal
    }
    print(">>> DATA BERHASIL DITAMBAHKAN! <<<")


def ubah_stok():
    print("___________________________________________________")
    print("          === UBAH DATA STOK DARAH ===            ")
    print("___________________________________________________")

    id_cari = input("Masukkan ID pendonor : ").strip().upper()

    if id_cari in stok_darah:
        print("DATA DITEMUKAN.")
        print("Nama           : ", stok_darah[id_cari]["Nama"])
        print("Golongan Darah : ", stok_darah[id_cari]["Golongan Darah"])
        print("Stok Saat Ini  : ", stok_darah[id_cari]["Jumlah Kantong"])

        jumlah_baru = input_jumlah("Jumlah Kantong Darah Baru : ")
        stok_darah[id_cari]["Jumlah Kantong"] = jumlah_baru
        print(">>> STOK BERHASIL DIPERBARUI! <<<")
    else:
        print("ID tidak ditemukan.")


def hapus_stok():
    print("___________________________________________________")
    print("          === HAPUS DATA STOK DARAH ===            ")
    print("___________________________________________________")

    hapus_data = input("Masukkan ID pendonor yang ingin dihapus : ").strip().upper()

    if hapus_data in stok_darah:
        konfirmasi = input("Yakin ingin menghapus stok darah ini? (ya/tidak): ").strip().lower()

        if konfirmasi == "ya":
            del stok_darah[hapus_data]
            print(">>> DATA BERHASIL DIHAPUS. <<<")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("ID tidak ditemukan.")

def menu_admin():
    while True:
        print()
        print("__________________________________________________")
        print("     SISTEM PENDATAAN DONOR DAN STOK DARAH PMI    ")
        print("                   (MENU ADMIN)                   ")
        print("__________________________________________________")
        print("MENU :")
        print("1. Lihat Semua Stok Darah")
        print("2. Tambah Data Stok Baru")
        print("3. Ubah Data Stok Darah")
        print("4. Hapus Data Stok Darah")
        print("5. Keluar")

        pilihan = input("PILIH MENU (1-5) : ")

        if pilihan == "1":
            tampilkan_stok()
        elif pilihan == "2":
            tambah_stok()
        elif pilihan == "3":
            ubah_stok()
        elif pilihan == "4":
            hapus_stok()
        elif pilihan == "5":
            break
        else: 
            print("Pilihan menu tidak valid. Silakan pilih 1-5.")


def menu_user():
    while True:
        print()
        print("__________________________________________________")
        print("     SISTEM PENDATAAN DONOR DAN STOK DARAH PMI    ")
        print("                   (MENU USER)                   ")
        print("__________________________________________________")
        print("MENU :")
        print("1. Lihat Semua Stok Darah")
        print("2. Keluar")

        pilihan = input("PILIH MENU (1-2): ")

        if pilihan == "1":
            tampilkan_stok()
        elif pilihan == "2":
            break
        else:
            print("Pilihan menu tidak valid. Silakan pilih 1-2.")


username, role = login()
print("Selamat Datang,", username, "| Role : ", role)
time.sleep(2)

if role == "ADMIN":
    menu_admin()
else:
    menu_user()

print("PROGRAM DONOR DARAH SELESAI. TERIMA KASIH!")