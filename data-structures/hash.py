class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

    def recreate(self):
        return Node(
            self.key,
            self.value,
        )


class HashTable:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._items  = 0
        self._data = [None] * self._capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        node = self._data[index]
        if node:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            #
            prev.next = Node(key, value)
        else:
            self._data[index] = Node(key, value)

        self._items += 1
        if self._items / self._capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        hsh = self._hash(key)
        node = self._data[hsh]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self._hash(key)
        node = self._data[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self._data[index] = node.next
                self._items -= 1
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self._items

    def getCapacity(self) -> int:
        return self._capacity

    def resize(self) -> None:
        new_cap = self._capacity * 2
        new_data = [None] * new_cap

        for node in self._data:
            while node:
                index = node.key % new_cap
                if new_data[index] is None:
                    new_data[index] = node.recreate()
                else:
                    new_node = new_data[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = node.recreate()
                node = node.next
       
        self._capacity = new_cap
        self._data = new_data

    def _hash(self, key: int) -> int:
        return key % self._capacity
