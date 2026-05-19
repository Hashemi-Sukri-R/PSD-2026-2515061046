# Implementasi Antrian Customer Service Bank Menggunakan QueueLinkedList

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
Ketika program baru dijalankan<br/>
<img width="229" height="129" alt="Idle" src="https://github.com/user-attachments/assets/19e8e2bd-edd3-4be4-8f56-e6099248f064" /><br/><br/>

User memasukan pilihan 1 dan menarik nomor nasabah<br/>
<img width="269" height="161" alt="inp1a" src="https://github.com/user-attachments/assets/d2ffe58d-2fc1-4220-b111-24d9677d3691" />
<img width="260" height="154" alt="inp1b" src="https://github.com/user-attachments/assets/20cdafc6-335d-4876-a6ea-91eb7dcac4fb" />
<img width="257" height="155" alt="inp1c" src="https://github.com/user-attachments/assets/4109883f-4205-4a16-b6b1-a0161bc523df" />
<img width="265" height="168" alt="inp1d" src="https://github.com/user-attachments/assets/3368d4ce-b0cb-4d79-a885-55bc0344c67f" />
<img width="251" height="157" alt="inp1e" src="https://github.com/user-attachments/assets/1a00020b-5c37-4019-9bd0-ced7afc32449" /> <br/>

User memasukan pilihan 2 dan memanggil nasabah<br/>
<img width="349" height="141" alt="inp2" src="https://github.com/user-attachments/assets/4cef5084-1d51-4358-8760-24b7d04024e5" /> <br/>

User memasukan pilihan 3 dan melihat antrian selanjutnya <br/>
<img width="212" height="135" alt="inp3" src="https://github.com/user-attachments/assets/5966ad97-5420-4c26-8fe4-7b339b6363da" /> <br/>

User memasukan pilihan 4 dan menunjukan seluruh antrian <br/>
<img width="235" height="207" alt="inp4" src="https://github.com/user-attachments/assets/ea7a2dcc-dda4-4eb4-ba3f-021980e5ed50" /> <br/>

User memasukan pilihan 5, menyelesaikan semua antrian dan menghentikan sistem <br/>
<img width="343" height="201" alt="inp5" src="https://github.com/user-attachments/assets/98c8a6bf-9b94-40c1-a412-824ce0781562" /> <br/>

## Link Video Penjelasan
Video penjelasan juga tersedia di [Youtube](https://youtu.be/q0OI1WNClck)
