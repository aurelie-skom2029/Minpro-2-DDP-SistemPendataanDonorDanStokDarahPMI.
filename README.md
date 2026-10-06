# Minpro-2-DDP-SistemPendataanDonorDanStokDarahPMI.

Nama : Diana Aurelia<br>
NIM  : 2609116105<br>
Kelas: C

Sistem Pendataan Donor dan Stok Darah PMI

Program ini dibuat menggunakan Python untuk membantu melakukan pendataan donor dan stok darah PMI.

Fitur Program untuk role admin :
* Melihat semua stok darah
* Menambahkan data donor
* Mengubah jumlah stok darah
* Menghapus data donor
* Keluar dari program
* Validasi input menu dan data

fitur untuk role user :
* Melihat semua stok darah
* Keluar dari program

Data yang digunakan terdiri dari:
* ID Pendonor
* Nama Pendonor
* Golongan Darah
* Jumlah Kantong Darah
* Tanggal Donor

 Konsep Python yang Digunakan
* Library (time, datetime, prettytable)
* While Loop
* If, Elif, dan Else
* Input dan Output
* CRUD (Create, Read, Update, Delete)

Tujuan :
Program ini dibuat sebagai mini project untuk menerapkan dasar-dasar pemrograman Python dalam sistem pendataan sederhana.

berikut output saya :
<img width="413" height="339" alt="Screenshot 2026-10-06 235408" src="https://github.com/user-attachments/assets/347c571c-787b-48c7-840e-19f5d879c886" />
<img width="389" height="473" alt="Screenshot 2026-10-06 235401" src="https://github.com/user-attachments/assets/012ee2a6-56ec-4fd5-b2e9-6b404504077d" />
<img width="483" height="466" alt="Screenshot 2026-10-06 235350" src="https://github.com/user-attachments/assets/fd5dc174-4c2c-4474-8c82-f1b2b28af5fe" />
<img width="575" height="378" alt="Screenshot 2026-10-06 235256" src="https://github.com/user-attachments/assets/a862278e-fb0d-4151-9c0e-02d1702bd9a1" />
<img width="343" height="292" alt="Screenshot 2026-10-06 235236" src="https://github.com/user-attachments/assets/c23d2a42-a87c-47ee-aa31-bd00b2393985" />
<img width="410" height="311" alt="Screenshot 2026-10-06 235226" src="https://github.com/user-attachments/assets/9c6c2004-7883-4bda-adda-5b90e83b6297" />
<img width="484" height="261" alt="Screenshot 2026-10-06 235217" src="https://github.com/user-attachments/assets/a0388705-db64-4abd-9dc4-3794f5f8a0ba" />
<img width="774" height="448" alt="Screenshot 2026-10-06 235159" src="https://github.com/user-attachments/assets/386b0e3a-e1c6-4771-8027-57263444195e" />
dari bawah bangg..

berikut flowchart saya
<img width="323" height="410" alt="Screenshot 2026-10-06 233118" src="https://github.com/user-attachments/assets/09c57823-d878-498d-b87c-358359cc1b90" />
penjelasan :
- Start
Program dimulai.

- Inisialisasi data
Program menyiapkan data awal stok darah dan data akun pengguna. Data akun terdiri dari akun admin dan user.

- Login
Pengguna memasukkan username dan password. Program kemudian mengecek apakah data login sesuai dengan akun yang tersedia.

- Login berhasil atau gagal
Jika username dan password benar, pengguna berhasil login.
Jika salah, program menampilkan pesan "LOGIN GAGAL" dan pengguna diminta mencoba kembali.

- Pengecekan role
Setelah berhasil login, program mengecek role pengguna, yaitu ADMIN atau USER.

- Menu Admin
Jika pengguna merupakan Admin, tersedia lima pilihan:
-Lihat semua stok darah
-Tambah data stok baru
-Ubah data stok darah
-Hapus data stok darah
-Keluar

- Menu User
Jika pengguna merupakan User, tersedia dua pilihan:
-Lihat semua stok darah
-Keluar

- Pengelolaan data
Lihat: menampilkan seluruh data stok darah dalam bentuk tabel.
Tambah: memasukkan ID, nama, golongan darah, jumlah kantong, dan tanggal.
Ubah: mencari ID pendonor kemudian mengubah jumlah kantong darah.
Hapus: mencari ID pendonor dan meminta konfirmasi sebelum data dihapus.

- Keluar
Jika pengguna memilih menu keluar, program kembali dari menu dan menampilkan pesan bahwa program telah selesai.

- End
Program berakhir.
