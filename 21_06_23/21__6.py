'''class Node:
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
a_llist.display()'''


'''#floyed algorithm 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        
    #insert a new node at start point
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def detectAndRemoveLoop(self):
        if self.head is None:#LL empty
            return
        if self.head.next is None:#LL has one node
            return
        p1 = self.head
        p2 = self.head
        
        while(p1 and p2 and p2.next):
            p1 = p1.next
            p2 = p2.next.next
            
            #if p1 and p2 meet at one point then that point is the meeting point
            #if there is a loop
            if p1 == p2:
                print("meeting point: ",p1.data)
                p1=self.head
                #finding the 1 st node
                while(p1.next!=p2.next):
                    p1 = p1.next
                    p2 = p2.next
                print("start of loop:",p2.next.data)
                p2.next = None #remove loop
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

llist = linkedlist()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
#creating loop
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist.printlist()
llist.detectAndRemoveLoop()
print("list after removing loop")
llist.printList()

#CIRCULAR LL
class Node: #creating a node
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL: #activating the node
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,end="")#temp.data means first node's data
                if temp.next!=None:
                    print("->",end="")#establishing linked
                temp=temp.next
                n5.next=self.head
obj=SLL() #node creation - intialising
n=Node(10) #so n.data class will be 10
obj.head=n  #assigning frst node as head
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()'''

'''#DELETION
class Node: #creating a node
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL: #activating the node
    def __init__(self):
        self.head=None
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None #last but before node's next
    def delete_position(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None   
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,end=" ")#temp.data means first node's data
                if temp.next!=None:
                    print('->',end=" ")
                temp=temp.next
obj=SLL() #node creation - intialising
n=Node(10) #so n.data class will be 10
obj.head=n  #assigning frst node as head
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
print()
obj.delete_begin()
obj.display()
print()
obj.delete_end()
obj.display()
print()
obj.delete_position(2)
obj.display()
print()'''

''''#SEARCH FOR A NODE SLL FAKE
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def search(self,num):
        temp = self.head
        while temp:
            temp.data=num
            print('yes')
            break
        temp = temp.next
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print('->',end="")
                temp=temp.next               
obj=SLL()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.search(60)
print()'''

#creaing node ORIGINAL
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def dispaly(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
    def search(self,num):
        temp=self.head
        flag=0
        while temp:
            if temp.data==num:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("element found")
        else:
            print("element not found")
obj=sll()
#node creation-initializing
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
obj.dispaly()
s=int(input("\nenter data to search:"))
obj.search(s)'''


#DOUBLE LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
            temp=temp.next               
obj=DLL()
n1=Node(10)
obj.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n3.prev=n2
n2.next=n3
obj.display()
print()








