class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            print("Head Node created:", self.head.value)
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)
        

dllist = DoubleLinkedList()
dllist.append("1st Node")

        
        