class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('is empty')
        else:
            current = self.head
            while current is not None:
                print(current.data, '--->', end=' ')
                current = current.next
    
    def add_begin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
            
    def add_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
     
    def add_after(self, data, x):
        current = self.head
        while current is not None:
            if current.data == x:
                break
            else:
                current = current.next
        if current is None:
            print('node is not present in LL')
        else:
            node = Node(data)
            node.next = current.next
            current.next = node
    
    def add_before(self, data, x):
        if self.head is None:
            print('Linked list is empty!')
            return
        if self.head.data == x:
            node = Node(data)
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current is not None:
            if current.next.data == x:
                break
            current = current.next
        if current.next is None:
            print('Node is not found!')
        else:
            node = Node(data)
            node.next = current.next
            current.next = node

    def insert_empty(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            print('Linked list is not empty!')

    def delete_begin(self):
        if self.head is None:
            print('LL is empty')
        else:
            self.head = self.head.next


    def delete_end(self):
        if self.head is None:
            print('LL is empty')
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print("can't delete LL is empty!")
            return 
        if x == self.head.data:
            self.head = self.head.next
            return
        node = self.head
        while node.next is not None:
            if x == node.next.data:
                break
            node = node.next
        if node.next is None:
            print('Node is not present!')
        else:
            node.next = node.next.next

            
            

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(20)


LL1.print_LL()

