# Implementasi Sistem Sorting Botol Bumbu Berdasarkan Tingginya

Program ini digunakan untuk mengurutkan botol bumbu berdasarkan tinggi botolnya menggunakan Insertion Sort   Pengguna dapat memasukan berapa banyak botol yang ingin di sorting dan berapa tinggi dari masing masing botol

## Source Code
<img width="717" height="811" alt="Source" src="https://github.com/user-attachments/assets/efcd3e4f-fca6-4a67-9aeb-afa5df9c87e7"/> <br/>
Berikut penjelasan dari kode diatas baris per baris  <br/><br/>
Baris 1: Mendefinisikan fungsi insertion_sort yang menerima input list arr dan jumlahnya n <br/>
Baris 2: <br/>
Baris 3: Memulai perulangan dari elemen kedua (indeks 1) hingga elemen terakhir <br/>
Baris 4: Menyimpan nilai elemen yang sedang diproses ke dalam variabel sementara temp <br/>
Baris 5: Menetapkan variabel j sebagai indeks elemen tepat di sebelah kiri i <br/>
Baris 6: Memulai perulangan while selama j belum habis dan elemen di kiri lebih besar dari temp <br/>
Baris 7: Menggeser elemen yang lebih besar tersebut ke posisi sebelah kanan <br/>
Baris 8: Mengurangi nilai j agar pengecekan berlanjut ke elemen di sebelah kirinya lagi <br/>
Baris 9: Menempatkan nilai temp ke posisi yang kosong setelah pergeseran selesai <br/>
Baris 10: <br/>
Baris 11: Mendefinisikan fungsi utama bernama main <br/>
Baris 12: Memulai blok try untuk menangani kesalahan (error) saat penginputan data <br/>
Baris 13: Mengambil input jumlah botol dari pengguna dan mengubahnya menjadi bilangan bulat (integer) <br/>
Baris 14: Menentukan tindakan jika terjadi kesalahan ValueError (misal input bukan angka) <br/>
Baris 15: Mencetak pesan peringatan bahwa input jumlah botol tidak valid <br/>
Baris 16: Menghentikan jalannya fungsi main karena terjadi kesalahan input <br/>
Baris 17: <br/>
Baris 18: Membuat sebuah list kosong bernama arr untuk menyimpan data tinggi botol <br/>
Baris 19: Mencetak kalimat instruksi pengisian tinggi botol kepada pengguna <br/>
Baris 20: Memulai perulangan sebanyak n kali untuk mengambil data setiap botol <br/>
Baris 21: Memulai perulangan while True agar program terus meminta input jika terjadi kesalahan ketik <br/>
Baris 22: Memulai blok try di dalam perulangan untuk mengecek validitas input tinggi tiap botol <br/>
Baris 23: Mengambil input tinggi botol spesifik (misal: botol ke-1) dan mengubahnya ke integer <br/>
Baris 24: Memasukkan nilai tinggi yang valid tersebut ke dalam list arr <br/>
Baris 25: Menghentikan perulangan while True karena input satu botol sudah berhasil diterima <br/>
Baris 26: Menentukan tindakan jika input tinggi botol bukan berupa angka <br/>
Baris 27: Mencetak pesan peringatan agar pengguna memasukkan angka yang benar <br/>
Baris 28:   <br/>
Baris 29: Mencetak isi list arr dalam kondisi awal (sebelum diurutkan) <br/>
Baris 30: Memanggil fungsi insertion_sort untuk memproses pengurutan list arr <br/>
Baris 31: Mencetak kalimat pembuka untuk menampilkan hasil akhir <br/>
Baris 32: Memulai perulangan untuk mengakses setiap elemen di dalam list yang sudah terurut <br/>
Baris 33: Mencetak setiap elemen list satu per satu secara menyamping <br/>
Baris 34: <br/>
Baris 35: Memanggil fungsi main() untuk menjalankan seluruh program dari awal <br/>

### Output Program
<img width="238" height="18" alt="input1" src="https://github.com/user-attachments/assets/35fbfb7a-b1c2-4d27-9ece-01fedb4a1232" />
Program akan meminta user berapa banyak botol yang akan diurutkan, disini saya mengisi 5 <br/><br/>

<img width="357" height="102" alt="input2" src="https://github.com/user-attachments/assets/84b2eaf1-a119-4c2c-88a1-26f77bf2d8b5" />
Program akan user mengisi tinggi botol sebanyak yang sudah di inputkan sebelumnya <br/><br/>

<img width="285" height="21" alt="Before" src="https://github.com/user-attachments/assets/56c9627a-c7ce-4902-becf-110f2b7a7e43" />
Menampilkan hasil yang belum di urutkan <br/><br/>

<img width="495" height="20" alt="After" src="https://github.com/user-attachments/assets/7a73bb9e-9bdc-4834-ba39-c63a6e58771f" />
Menampilkan hasil yang sudah di ururtkan <br/><br/>

### Link Video Penjelasan
Video penjelesan juga tersedia di [Youtube](https://youtu.be/kEQRneZsOSg)
