def code10_1():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    # 有向グラフとする
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].add(b)
        #無向グラフの場合はG[b].add(a)も追加
    print(G)
    return

class Edge(object):
    def __init__(self, to, w):
        self.to = to
        self.w = w

def code10_4():
    # 重み付きグラフの実装
    N, M = map(int, input().split()) # 頂点数, 辺の数
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        w = int(input())
        G[a].append(Edge(b, w))
    return

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
    
def code10_5() -> None:
    """
    heap
    parent >= children
    expected_out:
    7
    5
    11
    """
    h = Heap()
    for n in [5, 3, 7, 1]:
        h.push(n)
    print(h.top())
    h.pop()
    print(h.top())
    h.push(11)
    print(h.top())
    return

class Node:
    def __init__(self, data=None,parent=None,left=None,right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def push(self, x) -> None:
        self.size += 1
        if self.root is None:
            self.root = Node(data=x)
            return
        current_node = self.root
        while True:
            if current_node.data <= x:
                if current_node.right is None:
                    current_node.right = Node(x, current_node)
                    return
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = Node(x, current_node)
                    return
                else:
                    current_node = current_node.left
        return
    
    def search(self, x) -> bool:
        current_node = self.root
        while True:
            if current_node.data == x:
                return True
            elif current_node.data <= x and current_node.right:
                current_node = current_node.right
            elif current_node.data > x and current_node.left:
                current_node = current_node.left
            else:
                return False
        
    def remove(self, x) -> None:
        if not self.search(x):
            print("Given value is not in the tree.")
            return
        self.size -= 1
        current_node = self.root
        while True:
            if current_node.data == x:
                break
            elif current_node.data <= x:
                current_node = current_node.right
            elif current_node.data > x:
                current_node = current_node.left
        if current_node == self.root:
            self.root = current_node.right
            current_node.left.parent = self.root
            self.root.left = current_node.left
            return
        elif current_node == current_node.parent.left:
            if current_node.left and current_node.right:
                current_node.right.parent = current_node.left
                current_node.left.right = current_node.right
                current_node.left.parent = current_node.parent
                current_node.parent.left = current_node.left
            elif current_node.left:
                current_node.left.parent = current_node.parent
                current_node.parent.left = current_node.left
            else:
                current_node.right.parent = current_node.parent
                current_node.parent.left = current_node.right
            return
        else:
            if current_node.left and current_node.right:
                current_node.parent.right = current_node.right
                current_node.right.parent = current_node.parent
                current_node.left.parent = current_node.right
                current_node.right.left = current_node.left
            elif current_node.left:
                current_node.parent.left = current_node.left
                current_node.left.parent = current_node.parent
            else:
                current_node.right.parent = current_node.parent
                current_node.parent.left = current_node.right
            return
        
def binarysearchtree():
    bst = BinarySearchTree()
    values = [7, 2, 12, 5, 3, 6, 8, 11, 9, 15]
    for x in values:
        bst.push(x)
    print(bst.size)
    for x in [7, 2, 11]:
        bst.remove(x)
        print(bst.size)
    for x in [3, 6, 120]:
        print(f"{x} is in the tree." if bst.search(x) else f"{x} is not in the tree.")
    return

if __name__ == "__main__":
    # code10_1()
    # code10_5()
    binarysearchtree()