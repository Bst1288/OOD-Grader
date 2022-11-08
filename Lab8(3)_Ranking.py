class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def Ranking(self,node,data):
        if node == None:
            return 0

        rank = 0
        rank += self.Ranking(node.left,data)
        if node.data <= data:
            rank += 1
        rank += self.Ranking(node.right,data)
        return rank

T = BST()
inp,x = input('Enter Input : ').split('/')
for i in inp.split():
    root = T.insert(int(i))
T.printTree(root)
print('--------------------------------------------------')
print('Rank of',x,':',str(T.Ranking(root,int(x))))