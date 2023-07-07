#DELETION
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
print()