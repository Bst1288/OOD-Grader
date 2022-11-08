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
            print('*')
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        print('L*')
                        break
                    else:
                        print('L',end='')
                        cur = cur.left
                elif data >= cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        print('R*')
                        break
                    else:
                        print('R',end='')
                        cur = cur.right
        return self.root

t = BST()
inp =[int(i) for i in input('Enter Input : ').split()]
for i in range(0, len(inp)):
    t.insert(inp[i])