from math import radians


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doublyLL:
    def __init__(self):
        self.head = None


    def print_LL(self):
        if self.head is None:
            print('Linked list is empty!')
        else:
            current = self.head
            while current is not None:
                print(current.data, '-->', end=' ')
                current = current.next
    

    def print_LL_reverse(self):
        print()
        if self.head is None:
            print('Linked list is empty!')
        else:
            current = self.head
            while current.next is not None:
                print(current.data, '-->', end=' ')
                current = current.next

            while current is not None:
                print(current.data, '-->', end=' ')
                current = current.prev



    def insert_empty(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            print('Linked List is not empty!')

    def add_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    

    def add_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current


    def add_after(self, data, x):
        if self.head is None:
            print('LL is empty!')
        else:
            current = self.head
            while current is not None:
                if x == current.data:
                    break
                current = current.next
            if current is None:
                print('Given Node is not present in DLL')
            else:
                node = Node(data)
                node.next = current.next
                node.prev = current
                if current.next is not None:
                    current.next.prev = node
                current.next = node
    


    def add_before(self, data, x):
        if self.head is None:
            print('LL is empty!')
        else:
            current = self.head
            while current is not None:
                if x == current.data:
                    break
                current = current.next
            if current is None:
                print('Given Node is not present in DLL')
            else:
                node = Node(data)
                node.next = current
                node.prev = current.prev
                if current.prev is not None:
                    current.prev.next = node
                else:
                    self.head = node
                current.prev = node

                
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty don't delete!")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty don't delete!")
            return
        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.prev.next = None


    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty don't delete!")
            return     

        if self.head.next is None:
            if x == self.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head
        while current.next is not None:
            if x == current.data:
                break
            current = current.next
        if current.next is not None:
            current.next.prev = current.prev
            current.prev.next = current.next
        if current.data == x:
            current.prev.next = None 
        else:
            print("x is not present in dll")








dl1 = doublyLL()
dl1.insert_empty(10)
dl1.add_begin(20)
dl1.add_after(40,20)
dl1.add_end(30)
dl1.delete_by_value(20)
dl1.print_LL()