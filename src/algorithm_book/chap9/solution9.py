from collections import deque
from typing import Any


class Node(object):
    def __init__(self, data: Any, prev_node: Any = None, next_node: Any = None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(data=None, prev_node=None, next_node=None)

    def append(self, x: Any) -> None:
        node = Node(x)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node
        return
    
    def remove(self, x: Any):
        current_node = self.head
        if current_node and current_node.data == x:
            self.head = current_node.next
            current_node = None
            return

        while current_node and current_node.data != x:
            current_node = current_node.next

        if current_node is None:
            print("given value is not in the LinkedList.")
            return
        
        current_node.next.prev = current_node.prev
        current_node.prev.next = current_node.next
        return

class ElementryArithmetic:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def div(self, x, y):
        return x / y
    
    def culc(self, x, y, o):
        if o == "+":
            return self.add(x, y)
        elif o == "-":
            return self.sub(x, y)
        elif o == "*":
            return self.mul(x, y)
        elif o == "/":
            return self.div(x, y)
        
    
def solution9_2() -> None:
    rpn = [3, 4, "+", 1, 2, "-", "*"]
    stuck = deque([])
    ele = ElementryArithmetic()
    for c in rpn:
        if isinstance(c, str):
            y = stuck.pop()
            x = stuck.pop()
            stuck.append(ele.culc(x, y, c))
            continue
        stuck.append(c)
    print(stuck.pop())
    return

def solution9_3() -> None:
    N = int(input())
    kakko = input()
    stuck = deque([])
    corr = []
    for i in range(2*N):
        if kakko[i] == "(":
            stuck.append(i+1)
        elif kakko[i] == ")":
            if len(stuck) == 0:
                print("不整合")
                return
            else:
                corr.append((stuck.pop(), i+1))
    if len(stuck) != 0:
        print("不整合")
        return
    corr = sorted(corr, key=lambda x: x[0])
    print("整合しており，以下の括弧が対応している")
    print(*corr, sep=',')
    return
    

if __name__ == "__main__":
    # solution9_2()
    solution9_3()

        

        

        

        

        



