class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.height = 1
    
    def insert(self, value):
        new_node = Node(value)
        if(not self.root):
            self.root = new_node
        else:
            curr = self.root
            while(curr):
                if(value > curr.value):
                    if(curr.right):
                        curr = curr.right
                    else:
                        curr.right = new_node
                        break
                elif(value < curr.value):
                    if(curr.left):
                        curr = curr.left
                    else:
                        curr.left = new_node
                        break
                else:
                    print(f'{value} is already present in the binary search tree (BST). So, it is not possible to insert same value in the BST')
                    break
    
    def contains(self, value):
        if(not self.root):
            print('Their are no elements to check in the tree')
        else:
            curr = self.root
            while(curr):
                if(curr.value == value):
                    print(f'The element {value} is present in the binary search tree')
                    return True
                else:
                    if(value > curr.value):
                        curr = curr.right
                    else:
                        curr = curr.left
            print(f'The element {value} is not  present in the binary search tree')
            return False
    



bst = BST(2)
bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(30)
bst.insert(20)
bst.insert(100)
bst.contains(1000)
bst.contains(100)
bst.contains(1)
bst.contains(-1)