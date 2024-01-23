class Heap(object):


    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, x) -> None:
        self.heap.append(x)
        self.size += 1
        i = self.size - 1
        while i > 0:
            p = int((i-1)/2)
            if self.heap[p] >= x: break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x
        return
    
    def top(self) -> int:
        return self.heap[0] if self.size != 0 else -1
    
    def pop(self) -> None:
        if self.size == 0: return
        x = self.heap[-1]
        self.size -= 1
        i = 0
        while i * 2 + 1 < self.size:
            child_1, child_2 = i * 2 + 1, i * 2 + 2
            if child_2 < self.size and self.heap[child_2] > self.heap[child_1]:
                child_1 = child_2

            if self.heap[child_1] <= x:
                break
            self.heap[i] = self.heap[child_1]
            i = child_1
        self.heap[i] = x
        return

def solution10_2() -> None:
    test_case = [5, 6, 1]
    heap = Heap()
    for x in test_case:
        heap.push(x)
    print(heap.heap)
    return

def solution10_3() -> None:
    test_case = [5, 6, 1, 2, 7, 3, 4]
    heap = Heap()
    for x in test_case:
        heap.push(x)
    print(heap.heap)
    return

if __name__ == "__main__":
    solution10_2()
    solution10_3()