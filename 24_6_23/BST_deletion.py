'''LOGIC:
1.using "insert" create bst.
2.input node to be deleted
3.spot the node which u want to be deleted(search)
4.once u find the node,check it comes under which category of delete
5.apply delete concept
6.find inorder successor using separate function to replace with node to be deleted'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key,end=" ",)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < Node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
#given a non-empty binary
#search tree,return the node
#with min key value
#found in that tree,note that the
#entire tree doesnot need to be searched
#right subtree
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
#
def deleteNode(root,key):
    if root is None:
        return root
    #key<root it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key >root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root
""" let us create following BST
           50
        /      \
      30       70
     /  \     /  \
    20  40   60  80 """
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print("Inorder:")
inorder(root)
print("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder:modified tree")
inorder(root)
print ("\ndelete 30")
root = deleteNode(root, 30)
print ("Inorder:modified tree")
print ("\ndelete 50")
root = deleteNode(root, 50)
print ("Inorder:modified tree")
inorder(root)
