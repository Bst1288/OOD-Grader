class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
        

q = Queue()
booked,en = input('Enter Input : ').split('/')
booked_q = booked.split(' ')
en_q = en.split(',')

for i in booked_q:
    q.enqueue(i)
    
for i in en_q:
    if i[0] == 'E':
        str,num = i.split()
        q.enqueue(num)
    elif i[0] == 'D':
        q.dequeue()
i = 0
t = []
dup_list = q.items
while i < q.size():
    t.append(dup_list.count(dup_list[i]))
    i += 1
t2 = dict(zip(dup_list, t))
mode_list = { i for (i,j) in t2.items() if j == max(t) }
if len(mode_list) > 1:
    print('NO Duplicate')
elif len(mode_list) <= 1:
    print('Duplicate')
