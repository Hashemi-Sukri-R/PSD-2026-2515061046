class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nList Kode Pos Daerah Lampung")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()

    hashmap.insert(35118, "Enggal, Bandar Lampung")
    hashmap.insert(35125, "Sawah Lama, Bandar Lampung")
    hashmap.insert(35131, "Sukarame, Bandar Lampung")
    hashmap.insert(35144, "Rajabasa, Bandar Lampung")

    hashmap.display()
    hasil = hashmap.search(35125)
    if hasil is not None:
        print(f"\nKode Pos {hasil.key} ditemukan")
        print(f"Wilayah = {hasil.value}")
    else:
        print("\nKode Pos tidak ditemukan")

    hasil = hashmap.search(35145)
    if hasil is not None:
        print(f"\nKode Pos {hasil.key} masih ditemukan")
    else:
        print("\nKode Pos 35145 tidak ditemukan")

if __name__ == "__main__":
    main()
