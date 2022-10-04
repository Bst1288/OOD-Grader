class list:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self,data):
        h = self.head
        for i in range(len(self)):
            if h.data == data:
                return i
            h = h.next
        return -1
    
    def isIn(self,data):
        return self.indexOf(data) >= 0

    def nodeAt(self,i):
        h = self.head
        for j in range(0,i):
            h = h.next
        return h
    
    def append(self,data):
        if self.head is None:
            n = self.Node(data)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            self.addTail(data)

    def insertAfter(self,i,data):
        n = self.nodeAt(i)
        s = self.Node(data)
        s.next = n.next
        n.next = s
        self.size += 1
    
    def addTail(self,data):
        t = self.tail
        s = self.Node(data)
        t.next = s
        self.tail = s
        self.size += 1

    def removeTail(self) :
        if self.size > 0 :
          l = self.nodeAt(len(self) - 2)
          self.tail = l
          l.next = None
          self.size -= 1

    def deleteAfter(self,i) :
        if self.size > 0 :
          l = self.nodeAt(i)  
          l.next = l.next
          self.size -= 1

    def delete(self,i) :
        if self.size > 0 :
          if i == 0 :
            self.head = self.head.next
            self.size -= 1
          elif i == len(self) - 1 :
            self.removeTail()
          else :
            self.deleteAfter(i-1)

    def removeData(self,data) :
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)

    def addHead(self,data) :
        if self.isEmpty() :
          h = self.Node(data)
          self.head = h
          self.size += 1
        else :
          h = self.Node(data,self.head)
          self.head = h
          self.size += 1
    
    def __str__(self):
        s = ''
        p = self.head
        while p != None :
            if p.next !=None :
                s += str(p.data) + ' <- '
            else :
                s += str(p.data)
            p = p.next
        return s

count = 0
addData = False
linklist = list()
loco = list()

print(' *** Locomotive ***')
inp = input('Enter Input : ').split(' ')
for i in inp :
    linklist.append(int(i))
print('Before : ', end = '')
print(linklist)

if linklist.nodeAt(0).data != 0:
    for i in range(len(linklist)):
        if linklist.nodeAt(i).data == 0 or addData == True :
            loco.append(linklist.nodeAt(i).data)
            addData = True
        else :    
            count += 1
    for i in range(len(linklist)):
        if count >= 1 :
            loco.append(linklist.nodeAt(i).data)
            count -= 1
    print('After : ', end = '')
    print(loco)
else :
    print('After : ', end = '')
    print(linklist)