# Sistem Penyimpanan Nilai Ujian Mahaiswa Menggunakan Binary Search Tree
Program sederhana yang dibuat untuk menyimpan nilai mahasiswa. Program memiliki fitur untuk menambahkan, mencari, dan menampilkan nilai siswa secara terurut. Selain itu, program juga dapat menentukan nilai tertinggi, nilai terendah, dan total seluruh nilai dengan proses pencarian yang lebih cepat dan efisien.

## Source Code
<img width="778" height="2350" alt="code" src="https://github.com/user-attachments/assets/6ad2b906-84dc-47b3-a045-14f986dfc14f" /> <br/>
Berikut penjelasan singkat kode secara baris perbaris: <br/>
Baris 1: Membuat class Node sebagai tempat penyimpanan data pada BST.<br/>
Baris 2: Membuat constructor untuk class Node.<br/>
Baris 3: Menyimpan nilai data ke variabel key.<br/>
Baris 4: Membuat pointer kiri dengan nilai awal None.<br/>
Baris 5: Membuat pointer kanan dengan nilai awal None.<br/>
Baris 8: Membuat class BST.<br/>
Baris 9: Membuat constructor class BST.<br/>
Baris 10: Menginisialisasi root dengan nilai None.<br/>
Baris 12: Membuat fungsi untuk menambahkan node.<br/>
Baris 13: Mengecek apakah root kosong.<br/>
Baris 14: Membuat node baru jika root kosong.<br/>
Baris 15: Mengecek apakah nilai lebih kecil dari root.<br/>
Baris 16: Menambahkan node ke subtree kiri.<br/>
Baris 17: Mengecek apakah nilai lebih besar dari root.<br/>
Baris 18: Menambahkan node ke subtree kanan.<br/>
Baris 19: Mengembalikan root.<br/>
Baris 21: Membuat fungsi insert.<br/>
Baris 22: Memasukkan nilai ke BST mulai dari root.<br/>
Baris 24: Membuat fungsi pencarian node.<br/>
Baris 25: Mengecek apakah node kosong.<br/>
Baris 26: Mengembalikan False jika data tidak ditemukan.<br/>
Baris 27: Mengecek apakah data sama dengan root.<br/>
Baris 28: Mengembalikan True jika data ditemukan.<br/>
Baris 29: Mengecek apakah nilai lebih kecil dari root.<br/>
Baris 30: Mencari data pada subtree kiri.<br/>
Baris 31: Mencari data pada subtree kanan.<br/>
Baris 33: Membuat fungsi search.<br/>
Baris 34: Memanggil fungsi pencarian mulai dari root.<br/>
Baris 36: Membuat fungsi traversal inorder.<br/>
Baris 37: Mengecek apakah node kosong.<br/>
Baris 38: Menghentikan fungsi jika node kosong.<br/>
Baris 39: Menelusuri subtree kiri.<br/>
Baris 40: Menampilkan nilai node.<br/>
Baris 41: Menelusuri subtree kanan.<br/>
Baris 43: Membuat fungsi mencari nilai minimum.<br/>
Baris 44: Mengecek apakah tree kosong.<br/>
Baris 45: Mengembalikan -1 jika kosong.<br/>
Baris 46: Menyimpan root ke variabel current.<br/>
Baris 47: Melakukan perulangan selama node kiri masih ada.<br/>
Baris 48: Berpindah ke node paling kiri.<br/>
Baris 49: Mengembalikan nilai minimum.<br/>
Baris 51: Membuat fungsi mencari nilai maksimum.<br/>
Baris 52: Mengecek apakah tree kosong.<br/>
Baris 53: Mengembalikan -1 jika kosong.<br/>
Baris 54: Menyimpan root ke variabel current.<br/>
Baris 55: Melakukan perulangan selama node kanan masih ada.<br/>
Baris 56: Berpindah ke node paling kanan.<br/>
Baris 57: Mengembalikan nilai maksimum.<br/>
Baris 59: Membuat fungsi menjumlahkan seluruh node.<br/>
Baris 60: Mengecek apakah node kosong.<br/>
Baris 61: Mengembalikan 0 jika kosong.<br/>
Baris 62: Menjumlahkan seluruh nilai node secara rekursif.<br/>
Baris 64: Membuat fungsi utama program.<br/>
Baris 65: Membuat objek BST.<br/>
Baris 66: Membuat variabel pilihan menu.<br/>
Baris 67: Melakukan perulangan menu selama pilihan bukan 10.<br/>
Baris 68: Menampilkan judul menu.<br/>
Baris 69: Menampilkan menu input nilai.<br/>
Baris 70: Menampilkan menu cari nilai.<br/>
Baris 71: Menampilkan menu urutan nilai.<br/>
Baris 72: Menampilkan menu nilai minimum.<br/>
Baris 73: Menampilkan menu nilai maksimum.<br/>
Baris 74: Menampilkan menu total nilai.<br/>
Baris 75: Menampilkan menu keluar.<br/>
Baris 76: Mencoba menerima input user.<br/>
Baris 77: Mengubah input menjadi integer.<br/>
Baris 78: Menangani error jika input bukan angka.<br/>
Baris 79: Menampilkan pesan input tidak valid.<br/>
Baris 80: Mengulangi menu.<br/>
Baris 82: Mengecek apakah user memilih menu 1.<br/>
Baris 83: Mencoba menerima input nilai.<br/>
Baris 84: Mengubah input menjadi integer.<br/>
Baris 85: Memasukkan nilai ke BST.<br/>
Baris 86: Menampilkan pesan berhasil.<br/>
Baris 87: Menangani error input.<br/>
Baris 88: Menampilkan pesan input tidak valid.<br/>
Baris 89: Mengecek apakah user memilih menu 2.<br/>
Baris 90: Mencoba menerima input pencarian nilai.<br/>
Baris 91: Mengubah input menjadi integer.<br/>
Baris 92: Mengecek apakah nilai ditemukan.<br/>
Baris 93: Menampilkan pesan ditemukan.<br/>
Baris 94: Menjalankan kondisi jika nilai tidak ditemukan.<br/>
Baris 95: Menampilkan pesan tidak ditemukan.<br/>
Baris 96: Menangani error input.<br/>
Baris 97: Menampilkan pesan input tidak valid.<br/>
Baris 98: Mengecek apakah user memilih menu 3.<br/>
Baris 99: Menampilkan tulisan inorder.<br/>
Baris 100: Menampilkan data BST secara urut.<br/>
Baris 101: Membuat baris baru.<br/>
Baris 102: Mengecek apakah user memilih menu 4.<br/>
Baris 103: Menampilkan nilai minimum.<br/>
Baris 104: Mengecek apakah user memilih menu 5.<br/>
Baris 105: Menampilkan nilai maksimum.<br/>
Baris 106: Mengecek apakah user memilih menu 6.<br/>
Baris 107: Menampilkan jumlah seluruh nilai node.<br/>
Baris 108: Mengecek apakah user memilih menu 7.<br/>
Baris 109: Menampilkan pesan program selesai.<br/>
Baris 110: Menjalankan kondisi jika pilihan menu salah.<br/>
Baris 111: Menampilkan pesan pilihan tidak valid.<br/>
Baris 114: Mengecek apakah file dijalankan langsung.<br/>
Baris 115: Menjalankan fungsi main().<br/>

## Output Code
Menu yang muncul ketika program dijalankan <br/>
<img width="149" height="155" alt="idle" src="https://github.com/user-attachments/assets/a689e850-42f8-43c4-ba6d-568bbd0638ee" /><br/>

Ketika pengguna memasukan pilihan 1 maka, program akan meminta nilai yang ingin di input. Di sini saya memasukan nilai sebanyak 7 kali. <br/>
<img width="227" height="191" alt="out1a" src="https://github.com/user-attachments/assets/c94625f1-4e6e-40c4-9f07-0a228fa07400" />
<img width="216" height="194" alt="out1b" src="https://github.com/user-attachments/assets/68a26cbc-f0a9-4534-82d5-2c97e9534802" />
<img width="213" height="189" alt="out1c" src="https://github.com/user-attachments/assets/16c1713a-baf9-4399-9105-13f554e4d890" />
<img width="219" height="198" alt="out1d" src="https://github.com/user-attachments/assets/6001aa83-2179-4932-928e-6d4965cddf9f" />
<img width="215" height="195" alt="out1e" src="https://github.com/user-attachments/assets/0eed6a66-1bda-4909-90a8-0fec01e4fac8" />
<img width="215" height="190" alt="out1f" src="https://github.com/user-attachments/assets/b431771b-4383-486d-a40c-c0b38c135b89" />
<img width="207" height="190" alt="out1g" src="https://github.com/user-attachments/assets/ff47e440-dc9f-423a-87fe-ac13455fd173" /> <br/>

Ketika pengguna memasukan pilihan 2 maka, program akan meminta nilai yang ingin. Di cari di sini saya mencari nilai 43. <br/>
<img width="161" height="191" alt="out2a" src="https://github.com/user-attachments/assets/9a7c2507-d67a-4cce-8ee7-36335bf101a8" />

Ketika pengguna memasukan pilihan 3 maka, program akan mengurutkan nilai dari yang terkecil hingga terbesar. <br/>
<img width="224" height="182" alt="out3" src="https://github.com/user-attachments/assets/b85e88ad-a0b1-415a-bbcd-38de733a7364" /><br/>

Ketika pengguna memasukan pilihan 4 maka, program akan mangambil nilai paling rendah di dalam tree. <br/>
<img width="137" height="177" alt="out4" src="https://github.com/user-attachments/assets/00c619d5-a69d-4f69-8e70-b26427094465" /> <br/>

Ketika pengguna memasukan pilihan 5 maka, program akan mangambil nilai paling tinggi di dalam tree. <br/>
<img width="138" height="182" alt="out5" src="https://github.com/user-attachments/assets/7bbfbe66-74e2-4eba-b271-d294509a26d4" /> <br/>

Ketika pengguna memasukan pilihan 6 maka, program akan manjumlahkan seluruh nilai di dalam tree. <br/>
<img width="145" height="179" alt="out6" src="https://github.com/user-attachments/assets/75faa74a-36fd-458b-8bbc-7981ebec4516" /> <br/>

Ketika pengguna memasukan pilihan 7 maka, program akan selesai dan berhenti. <br/>
<img width="337" height="190" alt="out7" src="https://github.com/user-attachments/assets/9cafe368-aeb3-4679-8ea9-fc61da1def09" /> 


## Link Video Penjelasan
Video penjelasan juga tersedia di [Youtube](https://youtu.be/LEux0hg2q9Y)
