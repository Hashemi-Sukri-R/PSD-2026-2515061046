# implementasi Customer Service Bank menggunakan QueueLinkedList

## Source Code
<img width="738" height="2046" alt="Source" src="https://github.com/user-attachments/assets/5b495d78-62dc-4bbb-9250-63a2409cbf33" /><br/>
Berikut penjelasan singkat baris perbaris: <br/><br/>
Baris 1 : Membuat class Node untuk menyimpan data antrean.<br/>
Baris 2 : Constructor untuk menginisialisasi node baru.<br/>
Baris 3 : Menyimpan data ke dalam node.<br/>
Baris 4 : Membuat penunjuk ke node berikutnya dengan nilai awal kosong.<br/>
Baris 7 : Membuat class QueueLinkedList untuk queue berbasis linked list.<br/>
Baris 8 : Constructor untuk inisialisasi queue.<br/>
Baris 9 : Pointer depan queue diatur kosong.<br/>
Baris 10 : Pointer belakang queue diatur kosong.<br/>
Baris 12 : Method untuk mengecek apakah queue kosong.<br/>
Baris 13 : Mengembalikan nilai True jika queue kosong.<br/>
Baris 15 : Method untuk menambahkan data ke queue.<br/>
Baris 16 : Membuat node baru berisi data yang dimasukkan.<br/>
Baris 18 : Mengecek apakah queue kosong.<br/>
Baris 19 : Jika kosong, node baru menjadi antrean depan.<br/>
Baris 20 : Node baru juga menjadi antrean belakang.<br/>
Baris 21 : Jika queue tidak kosong.<br/>
Baris 22 : Menghubungkan node belakang lama ke node baru.<br/>
Baris 23 : Memindahkan pointer belakang ke node baru.<br/>
Baris 25 : Menampilkan pesan bahwa nasabah mengambil antrean.<br/>
Baris 27 : Method untuk mengambil antrean depan.<br/>
Baris 28 : Mengecek apakah queue kosong.<br/>
Baris 29 : Menampilkan pesan bahwa antrean kosong.<br/>
Baris 30 : Menghentikan proses method.<br/>
Baris 32 : Menyimpan antrean depan sementara ke variabel temp.<br/>
Baris 33 : Menampilkan nasabah yang dipanggil.<br/>
Baris 35 : Memindahkan pointer depan ke node berikutnya.<br/>
Baris 37 : Mengecek apakah queue menjadi kosong.<br/>
Baris 38 : Jika kosong, pointer belakang juga dikosongkan.<br/>
Baris 40 : Method untuk melihat antrean depan tanpa menghapusnya.<br/>
Baris 41 : Mengecek apakah queue kosong.<br/>
Baris 42 : Menampilkan pesan antrean kosong.<br/>
Baris 43 : Menghentikan method.<br/>
Baris 45 : Menampilkan data antrean paling depan.<br/>
Baris 47 : Method untuk menampilkan semua antrean.<br/>
Baris 48 : Mengecek apakah queue kosong.<br/>
Baris 49 : Menampilkan pesan antrean kosong.<br/>
Baris 50 : Menghentikan method.<br/>
Baris 52 : Menampilkan judul daftar antrean.<br/>
Baris 53 : Menyimpan pointer depan ke variabel bantu current.<br/>
Baris 55 : Perulangan selama node masih ada.<br/>
Baris 56 : Menampilkan data antrean saat ini.<br/>
Baris 57 : Berpindah ke node berikutnya.<br/>
Baris 60 : Function utama program.<br/>
Baris 61 : Membuat objek queue dari class QueueLinkedList.<br/>
Baris 62 : Perulangan program tanpa batas.<br/>
Baris 63 : Menampilkan judul menu program.<br/>
Baris 64 : Menampilkan menu ambil antrean.<br/>
Baris 65 : Menampilkan menu panggil nasabah.<br/>
Baris 66 : Menampilkan menu lihat antrean depan.<br/>
Baris 67 : Menampilkan menu tampilkan semua antrean.<br/>
Baris 68 : Menampilkan menu keluar program.<br/>
Baris 70 : Menerima input pilihan menu dari pengguna.<br/>
Baris 72 : Mengecek apakah pengguna memilih menu 1.<br/>
Baris 73 : Mencoba menjalankan input angka.<br/>
Baris 74 : Meminta nomor nasabah dan mengubahnya menjadi integer.<br/>
Baris 75 : Menangani error jika input bukan angka.<br/>
Baris 76 : Menampilkan pesan kesalahan input.<br/>
Baris 77 : Mengulang kembali ke menu awal.<br/>
Baris 78 : Menambahkan nomor nasabah ke queue.<br/>
Baris 80 : Mengecek apakah pengguna memilih menu 2.<br/>
Baris 81 : Memanggil antrean depan.<br/>
Baris 83 : Mengecek apakah pengguna memilih menu 3.<br/>
Baris 84 : Menampilkan antrean paling depan.<br/>
Baris 86 : Mengecek apakah pengguna memilih menu 4.<br/>
Baris 87 : Menampilkan seluruh antrean.<br/>
Baris 89 : Mengecek apakah pengguna memilih menu 5.<br/>
Baris 90 : Selama queue belum kosong.<br/>
Baris 91 : Menghapus antrean satu per satu.<br/>
Baris 93 : Menampilkan pesan program selesai.<br/>
Baris 94 : Menghentikan perulangan program.<br/>
Baris 96 : Jika pilihan menu tidak sesuai.<br/>
Baris 97 : Menampilkan pesan pilihan tidak valid.<br/>
Baris 100 : Menjalankan function utama program.<br/>
## Output Code

## Link Video Penjelasan
