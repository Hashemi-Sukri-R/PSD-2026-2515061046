def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def main():
    try:
        n = int(input("Masukkan jumlah botol bumbu: "))
    except ValueError:
        print("Input tidak valid! Masukkan angka untuk jumlah elemen.")
        return

    arr = []
    print(f"Masukkan tinggi masing-masing {n} botol (dalam cm):")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Tinggi botol ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print(f"Urutan awal rak: {arr}")
    insertion_sort(arr, n)
    print("Urutan rak setelah Insertion Sort (dari terpendek):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")

main()