class IndexedTree:
    '''
    A binary search tree with the following properties:
     * log(n) insertion
     * log(n) deletion
     * log(n) lookup by index
    '''
    def __init__(self, value):
        self.size = 1
        self.value = value
        self.left = self.right = singleton_empty_indexed_tree

    def insert(self, value):
        if self.value > value:
            self.left = self.left.insert(value)
        else:
            self.right = self.right.insert(value)
        self.size += 1

        return self

    def get(self, index):
        '''
        Basic idea is that the size of your left child determines your current index
        '''
        if self.left.size == index:
            return self.value
        elif self.left.size > index:
            return self.left.get(index)
        else:
            return self.right.get(index - self.left.size - 1)

    def remove(self, value):
        '''
        cases:
         * if found, then remove from right child and replace root
         * otherwise recurse appropriately
        '''
        if self.value == value:
            self.value = self.right.leftmostchild()
            if self.value is None:
                return self.left
            else:
                self.right = self.right.remove(self.value)
        elif self.value > value:
            self.left = self.left.remove(value)
        else:
            self.right = self.right.remove(value)

        self.size -= 1
        return self

    def leftmostchild(self):
        return self.left.leftmostchild() or self.value
        
    def __str__(self, level=0):
        ret = "\t"*level+f"{self.value}, {self.size}\n"
        ret += self.left.__str__(level+1) + self.right.__str__(level+1)
        return ret

    def __repr__(self):
        return self.__str__()

class EmptyIndexedTree(IndexedTree):
    def __init__(self):
        self.size = 0

    def insert(self, value):
        return IndexedTree(value)

    def get(self, index):
        raise NotImplementedError

    def leftmostchild(self):
        pass

    def __str__(self, level=0):
        return "\t"*level+"E"

singleton_empty_indexed_tree = EmptyIndexedTree()