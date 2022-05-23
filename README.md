# Tugas Seleksi Awal Internship Studycle

## Deskripsi
Program sederhana ini akan mengecek apakah masukan yang diberikan membentuk sebuah persegi atau tidak. Masukan berupa sebuah koordinat titik dalam 2D. Program ditulis dalam bahasa Python.

## How It Works
Setelah program menerima input titik koordinat dari pengguna, seluruh titik tersebut akan dikumpulkan ke dalam satu buat list. List tersebut akan masuk sebagai argumen ke dalam fungsi isThereSquare(). Fungsi ini mengecek apakah terdapat persegi yang bisa dibentuk dari titik-titik yang dimasukkan. Ini secara implisit juga menyatakan bahwa jumlah titik yang dimasukkan minimal berjumlah 4. 

Dari n buah titik tersebut (dengan asumsi n >= 4), akan dilakukan iterasi sebanyak nC4 (n kombinasi 4) kali untuk mengecek seluruh kemungkinan titik input ada yang membentuk persegi. Seluruh kemungkinan tersebut akan dicek menggunakan fungsi isSquare() yang menerima masukkan 4 tuple berisi titik-titik input. 

Pengecekan dalam isSquare() dilakukan dengan mencari apakah titik-titik tersebut jika dihubungkan akan membentuk 4 sudut dengan besar masing-masing 90 derajat dan seluruh sisi memiliki panjang yang sama. Jika kedua hal ini dipenuhi, isSquare() akan mengembalikan True dan mengembalikan False jika sebaliknya.

## How to Execute
Untuk menjalankan program, pastikan python3 sudah terpasang pada perangkat. Jika sudah, download repository ini dalam bentuk zip lalu buka file zipnya. Setelah itu, buka terminal lalu arahkan directory ke directory file zip yang sudah di-uncompress. Jalankan perintah berikut pada terminal

```
python3 persegi.py
```
Program akan meminta masukkan titik-titik koordinat dari pengguna. Untuk setiap titik, masukkan koordinat titik sumbu x dan y secara terpisah dan setiap satu titik telah dimasukkan, program akan menanyakan pengguna apakah masih ingin memasukkan titik baru. Jika pengguna memilih untuk tidak melanjutkan pemasukkan titik, program akan memulai eksekusi dan menentukan apakah ada persegi yang bisa dibentuk dari titik-titik yang dimasukkan. Hasil eksekusi akan di-print pada terminal.


## Author
Rafidika Samekto