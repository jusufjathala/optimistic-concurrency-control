# optimistic-concurrency-control

<br>
Program membutuhkan Python versi 3.x
<br>
Cara penggunaan program
1. Jalankan program occ.py dengan perintah "python3 occ.py"
2. Masukkan nama file eksekusi transaksi (contoh: "test1.txt")

<br>
Contoh file eksekusi transaksi
t1 r a
t2 w b
t1 v
t2 v
* ti = transaksi ke-i
* r = operasi read
* w = operasi write
* v = operasi validasi

