# Pertemuan 07 Fungsi Python
Nama: Hikmah Azizah

NIM: 2225250086

Kelas: 3B

## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular dalam bahasa pemrograman Python.

## Cara Menjalankan
python3 praktik/utilitas_matematika.py

## Struktur Fungsi
- `luas_persegi_panjang(p, l)`: Menerima parameter panjang (`p`) dan lebar (`l`), mengembalikan nilai luas persegi panjang.
- `luas_segitiga(a, t)`: Menerima parameter alas (`a`) dan tinggi (`t`), mengembalikan nilai luas segitiga.
- `jumlah_n(n)`: Menerima parameter integer nonnegatif `n`, menghitung total penjumlahan bilangan dari 1 sampai n menggunakan perulangan.
- `faktorial(n)`: Menerima parameter integer nonnegatif `n`, menghitung nilai faktorial menggunakan perulangan.
- `tampilkan_menu()`: Menampilkan pilihan menu operasi matematika interaktif kepada pengguna.

## Hasil Pengujian
| Operasi | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Luas persegi panjang | p=8, l=5 | 40 | 40 | Lulus |
| Luas segitiga | a=10, t=6 | 30.0 | 30.0 | Lulus |
| Jumlah 1..n | n=10 | 55 | 55 | Lulus |
| Faktorial | n=5 | 120 | 120 | Lulus |
| Faktorial | n=0 | 1 | 1 | Lulus |

## Refleksi
Bagian program yang menjadi lebih sederhana setelah dipisah menjadi fungsi adalah logika pengelolaan menu utama (`main`) dan perhitungan matematika. Dengan memecah rumus-rumus ke dalam fungsi mandiri yang mengembalikan nilai (`return`), program utama terhindar dari duokasi kode, menjadi lebih mudah dibaca, serta sangat mudah diuji secara independen (*unit testing*).