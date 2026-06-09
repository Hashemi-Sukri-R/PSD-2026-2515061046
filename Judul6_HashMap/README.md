# Sistem Pencarian Wilayah Berdasarkan Kode Pos Menggunakan Hash Map
Sistem Pencarian Wilayah Berdasarkan Kode Pos Menggunakan Hash Map adalah sistem yang memanfaatkan struktur data Hash Map untuk menyimpan dan mencari informasi wilayah berdasarkan kode pos. Dalam sistem ini, kode pos berperan sebagai key dan nama wilayah sebagai value. Ketika pengguna memasukkan kode pos, fungsi hash akan menghitung indeks penyimpanan sehingga data wilayah dapat ditemukan dengan cepat tanpa harus memeriksa seluruh data satu per satu.
## Source Code
<img width="817" height="2017" alt="source" src="https://github.com/user-attachments/assets/dadce9d4-89da-421a-bdd8-2de3d7abba25" />
Berikut penjelasan singkat cara kerja sistem secara baris perbaris: <br/>
Baris 1: Mendefinisikan kelas untuk menyimpan status slot pada Hash Map. <br/>
Baris 2: Menentukan nilai status slot kosong (EMPTY).<br/>
Baris 3: Menentukan nilai status slot terisi (OCCUPIED).<br/>
Baris 4: Menentukan nilai status slot yang telah dihapus (DELETED).<br/>
Baris 6: Mendefinisikan kelas Entry untuk menyimpan data pada Hash Map.<br/>
Baris 7: Membuat konstruktor kelas Entry.<br/>
Baris 8: Menginisialisasi key dengan nilai kosong.<br/>
Baris 9: Menginisialisasi value dengan nilai kosong.<br/>
Baris 10: Mengatur status awal slot sebagai EMPTY.<br/>
Baris 12: Mendefinisikan kelas HashMapOpenAddressing.<br/>
Baris 13: Membuat konstruktor Hash Map dengan ukuran default 10.<br/>
Baris 14: Menyimpan ukuran tabel Hash Map.<br/>
Baris 15: Membuat tabel berisi objek Entry sebanyak ukuran yang ditentukan.<br/>
Baris 17: Mendefinisikan fungsi hash.<br/>
Baris 18: Menghitung indeks berdasarkan key menggunakan operasi modulo.<br/>
Baris 20: Mendefinisikan fungsi untuk menambahkan data.<br/>
Baris 21: Menghitung indeks awal dari key.<br/>
Baris 22: Menyimpan posisi slot yang berstatus DELETED.<br/>
Baris 23: Melakukan perulangan untuk proses probing.<br/>
Baris 24: Menghitung indeks saat probing.<br/>
Baris 25: Memeriksa apakah slot sedang terisi.<br/>
Baris 26: Memeriksa apakah key sudah ada.<br/>
Baris 27: Memperbarui value jika key ditemukan.<br/>
Baris 28: Mengembalikan nilai True jika update berhasil.<br/>
Baris 29: Memeriksa apakah slot berstatus DELETED.<br/>
Baris 30: Memastikan slot DELETED pertama belum tersimpan.<br/>
Baris 31: Menyimpan posisi slot DELETED pertama.<br/>
Baris 33: Menangani kondisi jika slot kosong ditemukan.<br/>
Baris 34: Memeriksa apakah ada slot DELETED yang dapat digunakan kembali.<br/>
Baris 35: Menggunakan slot DELETED tersebut.<br/>
Baris 36: Menyimpan key pada slot.<br/>
Baris 37: Menyimpan value pada slot.<br/>
Baris 38: Mengubah status slot menjadi OCCUPIED.<br/>
Baris 39: Mengembalikan nilai True karena data berhasil ditambahkan.<br/>
Baris 40: Memeriksa kembali apakah terdapat slot DELETED setelah probing selesai.<br/>
Baris 41: Menyimpan key pada slot DELETED.<br/>
Baris 42: Menyimpan value pada slot DELETED.<br/>
Baris 43: Mengubah status slot menjadi OCCUPIED.<br/>
Baris 44: Mengembalikan nilai True karena data berhasil ditambahkan.<br/>
Baris 45: Mengembalikan False jika tabel penuh.<br/>
Baris 47: Mendefinisikan fungsi pencarian data.<br/>
Baris 48: Menghitung indeks awal key yang dicari.<br/>
Baris 49: Melakukan probing untuk mencari data.<br/>
Baris 50: Menghitung indeks selama proses pencarian.<br/>
Baris 51: Memeriksa apakah slot kosong ditemukan.<br/>
Baris 52: Mengembalikan None karena data tidak ada.<br/>
Baris 53: Memeriksa apakah key ditemukan pada slot yang terisi.<br/>
Baris 54: Mengembalikan objek Entry yang ditemukan.<br/>
Baris 55: Mengembalikan None jika data tidak ditemukan.<br/>
Baris 57: Mendefinisikan fungsi penghapusan data.<br/>
Baris 58: Mencari data yang akan dihapus.<br/>
Baris 59: Memeriksa apakah data ditemukan.<br/>
Baris 60: Mengembalikan False jika data tidak ditemukan.<br/>
Baris 61: Mengubah status slot menjadi DELETED.<br/>
Baris 62: Mengembalikan True karena data berhasil dihapus.<br/>
Baris 64: Mendefinisikan fungsi untuk menampilkan isi Hash Map.<br/>
Baris 65: Menampilkan judul daftar kode pos.<br/>
Baris 66: Melakukan perulangan untuk seluruh slot tabel.<br/>
Baris 67: Menampilkan nomor indeks slot.<br/>
Baris 68: Memeriksa apakah slot kosong.<br/>
Baris 69: Menampilkan status EMPTY.<br/>
Baris 70: Memeriksa apakah slot telah dihapus.<br/>
Baris 71: Menampilkan status DELETED.<br/>
Baris 73: Menampilkan key dan value pada slot yang terisi.<br/>
Baris 76: Mendefinisikan fungsi utama program.<br/>
Baris 77: Membuat objek HashMapOpenAddressing.<br/>
Baris 79: Menambahkan data kode pos Enggal ke Hash Map.<br/>
Baris 80: Menambahkan data kode pos Sawah Lama ke Hash Map.<br/>
Baris 81: Menambahkan data kode pos Sukarame ke Hash Map.<br/>
Baris 82: Menambahkan data kode pos Rajabasa ke Hash Map.<br/>
Baris 84: Menampilkan seluruh isi Hash Map.<br/>
Baris 85: Mencari data dengan kode pos 35125.<br/>
Baris 86: Memeriksa apakah data ditemukan.<br/>
Baris 87: Menampilkan kode pos yang ditemukan.<br/>
Baris 88: Menampilkan wilayah yang sesuai dengan kode pos tersebut.<br/>
Baris 89: Menangani kondisi jika data tidak ditemukan.<br/>
Baris 90: Menampilkan pesan bahwa kode pos tidak ditemukan.<br/>
Baris 92: Mencari data dengan kode pos 35145.<br/>
Baris 93: Memeriksa apakah data ditemukan.<br/>
Baris 94: Menampilkan kode pos jika ditemukan.<br/>
Baris 95: Menangani kondisi jika data tidak ditemukan.<br/>
Baris 96: Menampilkan pesan bahwa kode pos 35145 tidak ditemukan.<br/>
Baris 98: Memastikan program dijalankan sebagai program utama.<br/>
Baris 99: Memanggil fungsi utama untuk menjalankan program.<br/>

## Output Code
<img width="292" height="276" alt="output" src="https://github.com/user-attachments/assets/98c0453a-8608-4bc4-84b7-fd3395d7621a" /><br/>
ketika program dijalankan, sistem akan menanmpilkan daftar kode pos yang sudah dimasukankan sebelumnya. Setika dicari dengan memasukan kode pos sebagai kuncinya kunci tersebut akan menampilkan wilayah dari kode pos tersebut. Seperti pada output yang ditunjukan, saya memasukan kunci 35125 maka akan keluar wilayah sawah lama. jika memasukan kunci/kode pos yang tidak ada pada daftar maka akan menampilkan "Kode pos tersebut tidak ditemukan"

## Link Video Penjelasan
Video penjelasan juga tersedia di [Youtube](youtube.com)
