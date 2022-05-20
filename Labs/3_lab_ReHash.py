import random


class HashCell:
    def __init__(self, key, value, collision_link=-1):
        self.key=key
        self.value=value
        self.collision_link=collision_link

    def __str__(self):
        return '{key = ' + str(self.key) + ', value = ' + str(self.value) + ', collision_link = ' + str(self.collision_link) + '}'

    def __repr__(self):
        return '{key = ' + str(self.key) + ', value = ' + str(self.value) + ', collision_link = ' + str(self.collision_link) + '}'

class HashTable:

    def __init__(self, capacity=3571):
        self.capcity = capacity
        self.hash_table = [None]*capacity
        self.free_cells=capacity

    def get_hash(self, key):
        return key%self.capcity

    def put(self, key, value):
        status = self.__cell_status(key=key)
        if status == -1:
            if self.free_cells <= 0:
                self.__plus_capacity()
            hash_val = self.get_hash(key)
            while status ==-1:
                hash_val = random.randint(1,self.capcity-1)
                status = self.__cell_status(hash=hash_val)
            self.hash_table[hash_val] = HashCell(key, value)
            self.hash_table[self.get_hash(key)].collision_link=hash_val
            self.free_cells = self.free_cells - 1
        else:
            self.hash_table[self.get_hash(key)] = HashCell(key,value)
            self.free_cells = self.free_cells - 1

    def find(self, key):
        cell = self.hash_table[self.get_hash(key)]
        if cell is not None:
            if cell.key==key:
                return cell
            else:
                return self.hash_table[cell.collision_link]
        else:
            return None

    def delete(self, key):
        self.hash_table.remove(self.find(key))

    def __cell_status(self, key = None, hash = None): #1-свободна, 0 - занята тем же ключем (обновление значения),-1 - занята
        if hash is None:
            hash_value = self.get_hash(key)
            if self.hash_table[hash_value] is None:
                return 1
            elif self.hash_table[hash_value].key==key:
                return 0
            elif self.hash_table[hash_value] is not None:
                return -1
        elif key is None:
            if self.hash_table[hash] is None:
                return 1
            else:
                return -1

    def __plus_capacity(self):
        hash_table2 = [None]*self.capcity
        self.hash_table = self.hash_table+hash_table2
        self.free_cells=self.capcity
        self.capcity*=2


array = {1: 2, 2: 3, 4: 5, 7: 8}
map = HashTable(capacity=5)
for key in array.keys():
    map.put(key, array[key])
print(map.find(7))
print(map.hash_table)
map.delete(7)
print(map.hash_table)