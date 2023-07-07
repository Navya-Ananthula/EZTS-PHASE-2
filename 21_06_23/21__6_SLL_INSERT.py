#SINLGE LINKED LIST INSERTION
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_llist=LinkedList()
n=int(input('How many elements would you like to insert'))
for i in range(n):
    data=int(input("enter data item"))
    a_llist.append(data)
print('the linked list: ',end='')
a_llist.display()


#SLL INSERT AT END USING DYNAMIC
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,position,data):
        np=Node(data)
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def append(self,data):
        if self.last_node is None:
            self_head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self_last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data.end = ' ')
            current = current.next
a_list = LinkedList()
n = int(input('How many elements would you like to insert'))
           
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.insert_position(2,1000)
obj.display()


#SLL INSERT AT POSITION
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_position(self,position,data):
        np=Node(data)
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.insert_position(2,1000)
obj.display()
        
   
   










