class DoublyLinkedList :
    class Node:
        def __init__(self, data, prev = None, next = None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.dummy = self.Node(None,None,None)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0

    def __str__(self):
        s = ''
        n = self.dummy.next
        for i in range(len(self)-1):
            s += str(n.data) + ' '
            n = n.next
        if str(n.data) != 'None':
            s += str(n.data)
        return s

    def reverse(self):
        s = ''
        n = self.nodeAt(len(self)-1)
        for i in range(len(self)-1):
            s += str(n.data) + ' '
            n = n.prev
        if str(n.data) != 'None':
            s += str(n.data)
        return s

    def __len__(self) :
        return self.size  

    def isEmpty(self) :
        return self.size == 0

    def indexOf(self, data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1

    def isIn(self, data) :
        return self.indexOf(data) >= 0

    def nodeAt(self, i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p

    def insert(self, q, data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1  

    def append(self, data) :
        self.insert(self.nodeAt(len(self)), data)

    def remove(self, q) :
        if self.isIn(q):
            q = self.nodeAt(self.indexOf(q))
            p = q.prev
            x = q.next
            p.next = x
            x.prev = p
            self.size -= 1
            return q
        else:
            return -1

    def delete(self,i) :
        self.remove(self.nodeAt(i))

inp = input('Enter Input (L1,L2) : ').split(' ')
l1 = str(inp[0]).split('->')
l2 = str(inp[1]).split('->')
linkedList1 = DoublyLinkedList()
linkedList2 = DoublyLinkedList()
for i in l1:
    linkedList1.append(i)
for i in l2:
    linkedList2.append(i)
print('L1    :', linkedList1)
print('L2    :', linkedList2)
print('Merge :', linkedList1, linkedList2.reverse())