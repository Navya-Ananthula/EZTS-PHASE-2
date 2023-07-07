#SINGLE LINKED LIST
#CREATING node-declaration & definition
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
