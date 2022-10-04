class LinkedList():
    class Node():
        def __init__(self, data, prev = None, next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
            
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

        def __str__(self):
            return str(self.data)
            
    def __init__(self, n):
        self.head = None
        self.tail = None
        self.n = n
        self.max_length = 1
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def length(self):
        return self.count

    def get_max_length(self):
        return str(self.max_length-1)

    def push(self, val):
        node = self.Node(val)
        if int(val) > 0:
            self.max_length = max(self.max_length, len(val))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count += 1
    
    def sort(self):
        temp = []
        if not self.isEmpty():
            while not self.isEmpty():
                temp.append(int(self.popFront()))
            for x in sorted(temp):
                self.pushFront(str(x))

    def pushBack(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next, node.prev = node, self.head
            self.head = node
        self.count += 1

    def pushFront(self, value):
        node = self.Node(value)
        if int(value) > 0:
            self.max_length = max(self.max_length, len(value))
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.prev, node.next = node, self.tail
            self.tail = node
        self.count+=1

    def popFront(self):
        temp = self.tail.data
        try:
            self.tail = self.tail.next
            self.tail.prev = None  
            self.count -= 1
        except:
            self.head = None
            self.tail = None
            self.count = 0
        return temp

    def __str__(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' -> '
            current = current.next
        return temp[:-3]

    def nodeAt(self,i) :          
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def report(self):
        temp = ''
        current = self.tail
        while current:
            temp += str(current.data) + ' '
            current = current.next
        return temp

    def redix_sort(self):
        box = []
        for i in range(10):
            box.append(LinkedList(0))
        print("------------------------------------------------------------")
        stop = False
        counter = 0
        for i in range(self.max_length+1):
            print("Round : " + str(i+1))
            while not self.isEmpty():
                temp = self.popFront()[::-1]
                try:
                    box[int(temp[i])].pushFront(temp[::-1])   
                except:
                    box[0].pushFront(temp[::-1])
            if box[0].length() == self.n:
                stop = True
            for j in range(10):
                box[j].sort()
                print(str(j) + ' : ' + box[j].report())
                while not box[j].isEmpty():
                    temp = box[j].popFront()
                    self.pushBack(temp)
            print("------------------------------------------------------------")
            counter += 1
            if stop:
                break
        self.max_length = counter

rs = input("Enter Input : ").split()
after = LinkedList(len(rs))
before = LinkedList(len(rs))
for x in rs:
    after.push(x)
    before.push(x)

after.redix_sort()
print(after.get_max_length() + ' Time(s)')
print('Before Radix Sort : ' + str(before))
print('After  Radix Sort : ' + str(after))