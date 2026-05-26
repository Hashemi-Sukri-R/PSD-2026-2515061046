class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    bst = BST()
    pilih = 0
    while pilih != 10:
        print("\n=== MENU ===")
        print("1. Masukan nilai")
        print("2. Cari nilai")
        print("3. Urutan nilai")
        print("4. Nilai Minimum")
        print("5. Nilai Maximum")
        print("6. Total nilai")
        print("7. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                x = int(input("Masukkan nilai: "))
                bst.insert(x)
                print(f"Nilai {x} berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                x = int(input("Cari nilai: "))
                if bst.search(x):
                    print("Ditemukan")
                else:
                    print("Tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()
        elif pilih == 4:
            print(f"Min: {bst.find_min(bst.root)}")
        elif pilih == 5:
            print(f"Max: {bst.find_max(bst.root)}")
        elif pilih == 6:
            print(f"Jumlah nilai: {bst.sum_nodes(bst.root)}")
        elif pilih == 7:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
