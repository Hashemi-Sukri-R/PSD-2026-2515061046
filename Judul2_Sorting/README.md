# Implementasi Sistem Sorting Botol Bumbu Berdasarkan Tingginya

Program ini digunakan untuk mengurutkan botol bumbu berdasarkan tinggi botolnya menggunakan Insertion Sort. Pengguna dapat memasukan berapa banyak botol yang ingin di sorting dan berapa tinggi dari masing masing botol.

## Source Code
<img width="717" height="811" alt="Source" src="https://github.com/user-attachments/assets/efcd3e4f-fca6-4a67-9aeb-afa5df9c87e7" /> <br/>
1. Fungsi insertion_sort(arr, n). <br/>
Ini adalah cara kerja dari algoritma pengurutannya.

```
def insertion_sort(arr, n):
      for i in range(1, n):
```
Kita mulai perulangan dari botol kedua (indeks 1) sampai botol terakhir. Kenapa? Karena botol pertama (indeks 0) dianggap sudah "terurut" sendirian di awal.

```
temp = arr[i]
        j = i - 1
```
temp: Kita mengambil botol yang sedang diperiksa dan menyimpannya sementara di variabel temp.
j: Kita menyiapkan variabel untuk mengecek botol-botol di sebelah kirinya.

```
while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
```
Selama botol di sebelah kiri arr[j] lebih tinggi daripada botol di tangan kita (temp), maka botol yang lebih tinggi itu digeser ke kanan arr[j+1] = arr[j]. Kita terus bergerak ke kiri (j -= 1) untuk mencari posisi yang pas.

```
arr[j + 1] = temp
```
Setelah menemukan tempat di mana botol di sebelah kiri sudah tidak lebih tinggi lagi (atau sudah sampai ujung paling kiri), kita masukkan botol yang ada di tangan (temp) ke posisi tersebut<br/><br/>

2. Membuat Fungsi main()
```
def main():
    try:
        n = int(input("Masukkan jumlah botol bumbu: "))
    except ValueError:
        print("Input tidak valid! Masukkan angka untuk jumlah elemen.")
        return
```
Program meminta jumlah botol. Jika kamu memasukkan huruf (bukan angka), blok except akan menangkap kesalahan tersebut dan menghentikan program

```
arr = []
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Tinggi botol ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
```
membuat array kosong yang akan di isi lewat perluangan while. didalam loop nya user akan diminta memasukan tinggi botol, jika input tinggi botol valid, ia masuk ke list arr dan break akan menghentikan perulangan input untuk botol tersebut, lanjut ke botol berikutnya.<br/><br/>

3. Eksekusi dan Output
```
print(f"Urutan awal rak: {arr}")
    insertion_sort(arr, n) # Memanggil fungsi sortir yang kita buat sebelumnya
```
Menampilkan urutan botol sebelum di ururtkan, lalu menjalankan prosedur pengurutan.

```
print("Urutan rak setelah Insertion Sort (dari terpendek):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")

main()
```
Mencetak "Urutan rak setelah Insertion Sort". Penggunaan end=" " berfungsi agar hasil cetakan memanjang ke samping, bukan membuat baris baru setiap kali mencetak angka.
for loop untuk mencetak angka dari list yang sudah diurutkan
main() di baris terakhir adalah perintah untuk memulai seluruh rangkaian proses di atas

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
Video penjelesan juga tersedia di [Youtube](https://youtu.be/RTQOh2pYqBY)
