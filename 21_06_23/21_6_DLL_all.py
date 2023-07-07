class Node:
    def _init_(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def _init_(self):
        self.head=None
    def insert_start(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_pos(self,position,data):
        np=Node(data)
        temp=self.head
        for i in range(1,position-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
    def delete_start(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        temp.prev=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next=prev.next
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print("<->",end="")
                temp=temp.next
o=dll()
n1=Node(10)
o.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n3.prev=n2
n2.next=n3
o.display()
print()
o.insert_start(0)
o.display()
print()
o.insert_end(40)
o.display()
print()
o.insert_pos(2,20)
o.display()
print()
o.delete_start()
o.display()
print()
o.delete_pos(4)
o.display()
print()
o.deleteatend()
o.display()
print()