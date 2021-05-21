# Parent class
class Heap:

    # Constructor
    def __init__(self, a: list):
        self.a = a
        self.length = len(a)
        self.heap_size = len(a)

    # Methods
    def parent(self, i: int) -> int:
        return (i - 1)//2

    def left(self, i: int) -> int:
        return 2*i + 1

    def right(self, i: int) -> int:
        return 2*i + 2

    def exchange(self, i: int, j: int) -> None:
        temp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = temp

    def max_heapify(self, i: int) -> None:
        l = Heap.left(self, i)
        r = Heap.right(self, i)
        if l < self.heap_size and self.a[i] < self.a[l]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.a[largest] < self.a[r]:
            largest = r
        if largest != i:
            Heap.exchange(self, largest, i)
            Heap.max_heapify(self, largest)

    def build_max_heap(self) -> None:
        self.heap_size = self.length
        for i in range(self.length//2, -1, -1):
            Heap.max_heapify(self, i)

    def heapsort(self) -> None:
        Heap.build_max_heap(self)
        for i in range(self.length - 1, 0, -1):
            Heap.exchange(self, 0, i)
            self.heap_size = self.heap_size - 1
            Heap.max_heapify(self, 0)


# Child class
class MaxPriorityQueue(Heap):

    # Constructor (using parent)
    def __init__(self, a: list):
        super().__init__(a)
        self.build_max_heap()

    # Methods
    def maximum(self) -> int:
        return self.a[0]

    def extract_max(self) -> int:
        if self.heap_size < 1:
            print('heap underflow')  # edge case
        maximum = self.a[0]  # extract max
        self.a[0] = self.a[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        MaxPriorityQueue.max_heapify(self, 0)  # repair heap condition
        return maximum

    def increase_key(self, i: int, key: int) -> None:
        if key < self.a[i]:
            print('new key is smaller than current key')
        self.a[i] = key  # set new key
        while i > 0 and self.a[MaxPriorityQueue.parent(self, i)] < self.a[i]:  # repair heap condition
            MaxPriorityQueue.exchange(self, i, MaxPriorityQueue.parent(self, i))
            i = MaxPriorityQueue.parent(self, i)

    def max_insert(self, key: int) -> None:
        import sys
        self.heap_size = self.heap_size + 1  # increase heap size
        self.a.append(-sys.maxsize)  # insert negative infinity node
        MaxPriorityQueue.increase_key(self, self.heap_size - 1, key)  # repair heap condition


if __name__ == "__main__":
    # create an arbitrary set
    a = [1, 3, 5, 6, 7]
    # create heap and (max) priority queue objects
    hp = Heap(a)
    pq = MaxPriorityQueue(a)
    # test any methods you want below
