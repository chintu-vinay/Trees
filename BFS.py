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
    
    def bfs(self):
        if(not self.root):
            print('Their are no elements in the binary search tree')
        else:
            nodes_qe = []
            res_qe = []
            curr = self.root
            nodes_qe.append(curr)
            while(len(nodes_qe) > 0):
                curr = nodes_qe.pop(0)
                res_qe.append(curr.value)
                if(curr.left is not None):
                    nodes_qe.append(curr.left)
                if(curr.right is not None):
                    nodes_qe.append(curr.right)
            print('The elements present in the binary search tree is ', res_qe)
    



bst = BST(2)
bst.insert(1)
bst.insert(3)
bst.insert(10)
bst.insert(30)
bst.insert(20)
bst.insert(100)

bst.bfs()