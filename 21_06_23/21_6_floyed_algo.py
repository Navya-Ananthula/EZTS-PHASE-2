#floyed algorithm 
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