class linkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) :
        return self.size  

    def isEmpty(self) :
        return self.size == 0

    def indexOf(self, data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1

    def isIn(self, data) :
        return self.indexOf(data) >= 0

    def nodeAt(self, i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def append(self, data):
        if self.head is None:
            n = self.Node(data)
            self.head = n
            self.tail = n
            self.next = None
            self.prev = None
            self.size += 1
        else:
            self.insertAfter(len(self)-1, data)

    def insertAfter(self, i, data):
        if len(self) == 0:
            self.addHead(data)
        else:
            if i < 0:
                if(-i > len(self)):
                    i = -1
                else:
                    i = len(self)+i-1
            elif i >= len(self):
                i = len(self)-1
            elif i == -1:
                self.addHead(data)
            else:
                p = self.nodeAt(i)
                q = self.Node(data)
                if len(self)-1 != i:
                    r = self.nodeAt(i+1)
                    r.prev = q

                q.next = p.next
                p.next = q
                q.prev = p

                if i == len(self)-1:
                    self.tail = q
                self.size += 1

    def addHead(self, data):
        if self.isEmpty():
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else:
            q = self.head
            p = self.Node(data)
            q.prev = p
            p.next = q
            self.head = p
            self.size += 1

    def deleteHead(self):
        q = self.head.next
        q.prev = None
        self.head = q
        self.size -= 1

    def deleteAfter(self, i):
        if len(self) > 0:
            q = self.nodeAt(i)
            q.next = q.next.next
            self.size -= 1

inp = input('Enter Input : ').split(',')
cursor = 0
lls = linkedList()
for i in inp:
    if i[0] == 'I':
        if cursor != 0:
            lls.insertAfter(cursor-1, i[2:])
        else:
            lls.addHead(i[2:])
        cursor += 1
    elif i[0] == 'L' and cursor > 0:
        cursor -= 1
    elif i[0] == 'R' and cursor < len(lls):
        cursor += 1
    elif i[0] == 'B' and cursor > 0:
        cursor -= 1
        lls.deleteAfter(cursor-1)
    elif i[0] == 'D' and cursor < len(lls):
        if cursor == 0:
            lls.deleteHead()
        else:
            lls.deleteAfter(cursor-1)

for i in range(len(lls)):
    if i == cursor:
        print('|', end=' ')
    print(lls.nodeAt(i).data, end=' ')
if cursor == len(lls):
    print('|', end=' ')