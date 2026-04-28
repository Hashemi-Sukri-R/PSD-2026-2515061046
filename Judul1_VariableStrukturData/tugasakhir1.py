def menu():
    print("1. Cek antrian pasien saat ini")
    print("2. Masukan pasien")
    print("3. Layanin pasien")
    print("4. Cek status pasien")
    print("5. Keluar program")

def main():
    pasien = []
    done = []
    run = True
    while run:
        menu()
        inp = int(input("Masukan angka yang ingin dipilih: "))
        if inp == 1:
            if len(pasien) == 0:
                print("Antrian masih kosong\n")
            else:
                print(pasien,"\n")
        
        elif inp == 2:
            try:
                banyak = int(input("Masukan banyak pasien: "))
            except ValueError:
                print("Tolong masukan angka")
                continue
            for i in range(banyak):
                nama = input("Masukan nama pasien: ")
                pasien.append(nama)
            print("Pasien sudah masuk\n")
        
        elif inp == 3:
            if len(pasien) == 0:
                print("List masih kosong")
            else:
                layani = int(input("Berapa banyak yang sudah dilayani: "))
                for i in range(layani):
                    after = pasien.pop(0)
                    done.append(after)
                print("Sudah di update\n")           
        
        elif inp == 4:
            print(f"Pasien yang masih di antrian: {pasien}")
            print(f"Pasien yang sudah dilayani: {done}\n")
        
        elif inp == 5:
            print("Program selesai\n")
            run = False
        
        else:
            print("Pilihan tidak valid\n")
            

main()