class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if not node:
            node = TreeNode(data)
            return node
        elif node.val > data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right, data)

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        
        balance = self.getBalance(node)
        if balance > 1 and data < node.left.val:
            print('Not Balance, Rebalance!')
            return self.rotateRight(node) 
        
        if balance < -1 and data >= node.right.val:
            print("Not Balance, Rebalance!")
            return self.rotateLeft(node) 
  
        if balance > 1 and data >= node.left.val:
            print("Not Balance, Rebalance!") 
            node.left = self.rotateLeft(node.left) 
            return self.rotateRight(node) 
  
        if balance < -1 and data < node.right.val:
            print("Not Balance, Rebalance!")  
            node.right = self.rotateRight(node.right) 
            return self.rotateLeft(node) 

        return node

    def rotateLeft(self, z): 
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        
        return y 

    def rotateRight(self, z): 
        y = z.left 
        T3 = y.right 

        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("===============")