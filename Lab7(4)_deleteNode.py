class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.data:
                    if cur.left == None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                elif val > cur.data:
                    if cur.right == None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
                else:
                    break
        return self.root

    def delete(self,r, data):
        if r is None:
            print("Error! Not Found DATA")
            return
        if self.root.left == None and self.root.right == None and self.root.data == data:
            self.root = None
        elif self.root.left == None and self.root.data == data :
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:
            self.root = self.root.left


        if r.data != data:
            if r.data > data:
                r.left = self.delete(r.left,data)
            else:
                r.right = self.delete(r.right,data)
        else:
            if r.left == None:
                r = r.right
                return r
            elif r.right == None:
                r = r.left
                return r
            else:
                c = r.right
                while c.left != None:
                    c = c.left
                r.data = c.data
                r.right = self.delete(r.right,c.data)
        return r
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    sym = i.split(' ')
    if sym[0] == 'i':
        print('insert ' + sym[1])
        tree.insert(int(sym[1]))
        printTree90(tree.root)
    elif sym[0] == 'd':
        print('delete '+ sym[1])
        tree.delete(tree.root, int(sym[1]))
        printTree90(tree.root)