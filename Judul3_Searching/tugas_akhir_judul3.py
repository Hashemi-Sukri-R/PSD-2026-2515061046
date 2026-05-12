def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["Sabun", "Shampoo", "Pasta Gigi", "Sabun", "Tisu", "Minyak", "Sabun", "Sikat Gigi", "Tisu"]
    n = len(data)
    
    print(f"Daftar produk di toko: {data}")
    target = input("Masukkan nama produk yang ingin dicari: ")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Produk '{target}' ditemukan sebanyak {counter} kali di toko.")
    else:
        print(f"Produk '{target}' tidak tersedia di toko.")

main()
