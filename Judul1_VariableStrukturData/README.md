# Implementasi Sistem Antrian Pasien pada Rumah Sakit

Program ini digunakan untuk mengatur antrian pasien di rumah sakit. Pengguna dapat menambahkan pasien, melihat daftar antrian, melayani pasien sesuai urutan kedatangan, serta melihat pasien yang sudah dilayani. Program berjalan melalui menu hingga pengguna memilih untuk keluar.

## Source Code
<img width="724" height="1172" alt="SC1" src="https://github.com/user-attachments/assets/4ca603a1-40a0-48e1-ba05-d351b060e18e" /> <br/>
1. Definisi Fungsi menu()
Fungsi ini bertugas hanya untuk menampilkan pilihan kepada pengguna.
```
def menu():
    print("1. Cek antrian pasien saat ini")
    print("2. Masukan pasien")
    print("3. Layanin pasien")
    print("4. Cek status pasien")
    print("5. Keluar program")
```
Ketika fungsi ini dipanggil, ia akan mencetak daftar pilihan menu ke layar. <br/>

2. Inisialisasi pada Fungsi main()
```
def main():
    pasien = []  # List untuk menyimpan nama pasien yang sedang mengantre
    done = []    # List untuk menyimpan nama pasien yang sudah selesai dilayani
    run = True   # Variabel kontrol (flag) agar program terus berjalan
```
* pasien: Digunakan sebagai queue utama.
* done: Digunakan sebagai histori/rekam medis sederhana untuk pasien yang sudah lewat.
* run: Selama variabel ini True, program tidak akan berhenti.

3. Perulangan Utama (Main Loop)
```
while run:
        menu() # Memanggil tampilan menu
        inp = int(input("Masukan angka yang ingin dipilih: ")) # Mengambil input pilihan user
```
Program masuk ke infinite loop yang hanya akan berhenti jika user memilih menu nomor 5. <br/>

4. Logika Menu 1: Cek Antrean
```
if inp == 1:
            if len(pasien) == 0:
                print("Antrian masih kosong\n")
            else:
                print(pasien,"\n")
```
Mengecek panjang list pasien. Jika 0, berarti tidak ada orang. Jika ada, tampilkan isi list tersebut. <br/>

5. Logika Menu 2: Masukkan Pasien
```
elif inp == 2:
            try:
                banyak = int(input("Masukan banyak pasien: ")) # Input jumlah pasien baru
            except ValueError:
                print("Tolong masukan angka") # Menangani jika user input huruf, bukan angka
                continue
            for i in range(banyak):
                nama = input("Masukan nama pasien: ")
                pasien.append(nama) # Menambahkan nama ke urutan paling belakang list
            print("Pasien sudah masuk\n")
```
Menggunakan try-except untuk mencegah program crash jika salah input. Pasien ditambahkan ke list menggunakan .append(), yang secara otomatis menaruh mereka di posisi paling akhir (belakang antrean). <br/>

6. Logika Menu 3: Layani Pasien
```
elif inp == 3:
            if len(pasien) == 0:
                print("List masih kosong")
            else:
                layani = int(input("Berapa banyak yang sudah dilayani: "))
                for i in range(layani):
                    after = pasien.pop(0) # MENGAMBIL elemen index 0 (paling depan)
                    done.append(after)    # Memindahkan pasien tersebut ke list 'done'
                print("Sudah di update\n")
```
Fungsi .pop(0) adalah kunci dari antrean. Ia mengambil pasien yang paling lama menunggu (indeks 0) dan menghapusnya dari list pasien. Pasien tersebut kemudian dipindahkan ke list done. <br/>

7. Logika Menu 4 & 5: Status dan Keluar
```
elif inp == 4:
            # Menampilkan kedua list untuk perbandingan
            print(f"Pasien yang masih di antrian: {pasien}")
            print(f"Pasien yang sudah dilayani: {done}\n")
        
        elif inp == 5:
            print("Program selesai\n")
            run = False # Mengubah flag menjadi False untuk menghentikan 'while run'
```
Menu ke 4 memberikan laporan lengkap kepada admin. Kamu bisa melihat siapa saja yang masih menunggu di list pasien dan siapa saja yang sudah selesai di list done. Ini berguna untuk sinkronisasi data dan menu 5 untuk menutup program dengan mengubah variabel run = False, sehingga loop berhenti <br/>

8. Penanganan Input Tidak Valid & Eksekusi Program
```
else:
            print("Pilihan tidak valid\n") # Jika user input angka selain 1-5

main() # Memanggil fungsi main agar program berjalan pertama kali
```
Baris else ini menangkap semua angka yang tidak ada di menu (misalnya user input angka 7, 0, atau 99). dan fungi main() untuk mengeksekusi program

### Output Program
Menu pada saat pertama kali program di jalankan
<img width="319" height="107" alt="Idle" src="https://github.com/user-attachments/assets/63020b19-01e9-4170-b0f6-527788cb516e" /> <br/>

Menu 1 ketika masih kosong
<img width="283" height="126" alt="empty1" src="https://github.com/user-attachments/assets/aa398347-b775-46af-adef-63e25ef2ffc3" /> <br/>

Menu 2
<img width="287" height="223" alt="input2" src="https://github.com/user-attachments/assets/8dc0e01f-44e2-4098-a780-56c3af572ff7" /> <br/>

Menu 1 ketika sudah di masukan
<img width="327" height="134" alt="item1" src="https://github.com/user-attachments/assets/d04d52a3-5c64-4ea3-a542-87b3db7e8d01" /> <br/>

Menu 3
<img width="283" height="142" alt="input3" src="https://github.com/user-attachments/assets/12bf97ee-b2af-4dfd-8239-11653e5ec849" /> <br/>

Menu 1 ketika beberapa pasien sudah dilayani
<img width="273" height="136" alt="current1" src="https://github.com/user-attachments/assets/6ba9c25f-ad19-472e-b0a5-953869515a9b" /> <br/>

Menu 4
<img width="424" height="161" alt="input4" src="https://github.com/user-attachments/assets/03494e02-d7f7-42da-8199-8eb3eee08dcc" /> <br/>

Menu 5
<img width="265" height="122" alt="input5" src="https://github.com/user-attachments/assets/0c890310-5705-476f-bc17-0437757a4440" /> <br/>


### Link Youtube Penjelasan
Video penjelesan juga tersedia di [Youtube](https://youtube.com)
