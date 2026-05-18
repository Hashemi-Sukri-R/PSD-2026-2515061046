class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Nasabah nomor'{x}' mengambil antrean")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        temp = self.front_ptr
        print(f"Nasabah nomor '{temp.data}' dipanggil ke Customer Service")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print(f"Antrean berikutnya: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrean kosong")
            return

        print("Daftar antrean nasabah:")
        current = self.front_ptr

        while current is not None:
            print("-", current.data)
            current = current.next


def main():
    queue = QueueLinkedList()
    while True:
        print("\n=== CUSTOMER SERVICE BANK ===")
        print("1. Ambil Antrean")
        print("2. Panggil Nasabah")
        print("3. Lihat Antrean Depan")
        print("4. Tampilkan Semua Antrean")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            try:
                nama = int(input("Masukkan nomor nasabah: "))
            except ValueError:
                print("Hanya menerima angka")
                continue
            queue.enqueue(nama)

        elif pilih == "2":
            queue.dequeue()

        elif pilih == "3":
            queue.peek()

        elif pilih == "4":
            queue.display()

        elif pilih == "5":
            while not queue.is_empty():
                queue.dequeue()

            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


main()
