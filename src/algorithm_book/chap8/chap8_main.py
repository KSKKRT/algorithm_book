from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.prev = previous_node

class SimpleLinkedList(object):

    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def insert(self, v: Node, p: Node) -> None:
        v.next = p.next
        p.next = v
        return
    
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "->", end='')
            current_node = current_node.next

class BidirectionalLinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = Node(head, next_node=None, previous_node=None)
        self.size = 0

    def printList(self) -> None:
        current_node = self.head.next
        while current_node:
            print(current_node.data, " -> ", end='')
            current_node = current_node.next
        print()
        return

    def append(self, data: Any) -> None:
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node
        return
    
    def remove(self, v: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == v:
            self.head = current_node.next
            current_node = None
            slef.size -= 1
            return
        
        while current_node and current_node.data != v:
            current_node = current_node.next

        if current_node is None:
            return
        
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node = None
        self.size -= 1
        return


def code8_4():
    names = [
        "yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"
    ]
    names = names[::-1]
    linkedlist = SimpleLinkedList()
    for i in range(len(names)):
        linkedlist.append(names[i])
        print(f"step{i+1}: ", end='')
        linkedlist.printList()
        print()

def code8_6():
    names = [
        "yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"
    ]
    names = names[::-1]
    linkedlist = BidirectionalLinkedList()
    for i in range(len(names)):
        linkedlist.append(names[i])

    print("削除前")
    linkedlist.printList()
    linkedlist.remove("watanabe")
    print("削除後")
    linkedlist.printList()
    return


if __name__ == "__main__":
    # code8_4()
    code8_6()


    
    
