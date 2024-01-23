class Stuck_list(object):
    def __init__(self):
        self.max = 100000000
        self.top = 0
        self.stuck = [0] * self.max

    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top == self.max
    
    def push(self, x):
        if self.isFull():
            print("Error: stuck is full.")
            return
        self.stuck[self.top] = x
        self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Error: stuck is empty.")
            return -1
        self.top -= 1
        return self.stuck[self.top]

class Queue_list(object):

    def __init__(self):
        self.max = 12
        self.head = 0
        self.tail = 0
        self.que = [0 for _ in range(self.max)]
        self.size = 0

    def isEmpty(self) -> bool:
        return self.head == self.tail
    
    def isFull(self) -> bool:
        return self.head == (self.tail+1) % self.max
    
    def enqueue(self, x) -> None:
        if self.isFull():
            print("Error: Queue is full.")
            return
        self.que[self.tail] = x
        self.tail += 1
        self.size += 1
        if self.tail == self.max: self.tail = 0
        return
    
    def dequeue(self):
        if self.isEmpty():
            print("Error: queue is empty.")
            return -1
        res = self.que[self.head]
        self.head += 1
        self.size -= 1
        if self.head == self.max: self.head = 0
        return res


def code9_1() -> None:
    s = Stuck_list()
    s.push(3)
    s.push(5)
    s.push(7)
    print(s.pop())
    print(s.pop())
    s.push(9)
    print(s.top)
    return

def code9_2() -> None:
    q = Queue_list()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(9)
    print(q.que)
    print(q.size)
    for n in [11, 12, 13, 14, 15, 156, 98, 33, 92, 102]:
        q.enqueue(n)
    print(q.que)
    print(q.size)
    return

# collections.deque による実装
def code9_3() -> None:
    from collections import deque
    stuck = deque([])
    queue = deque([])
    components = [3, 5, 6, 7, 8, 9]
    for i in components:
        stuck.append(i)
        queue.append(i)
    for _ in range(3):
        print(f"stuck out: {stuck.pop()}, queue out: {queue.popleft()}")
    for _ in range(3):
        stuck.pop()
        queue.popleft()
    try:
        queue.popleft()
    except IndexError:
        print("Queue is empty.")
    return

if __name__ == "__main__":
    # code9_1()
    # code9_2()
    code9_3()


        