'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา
A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK
P  ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น -1
*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empt
'''
class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        s = 'Value in Stack = '
        for ele in self.items:
            s += str(ele)+' '
        return s

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

S = input('Enter Input : ').split(',')
stack = Stack()

for symbol in S:
    if symbol[0] == "A":
        int,temp = symbol.split()
        stack.push(temp)
        print('Add =' , stack.peek() , 'and Size =' , stack.size())
    elif symbol[0] == 'P':
        if stack.isEmpty():
            print('-1')
        else:
            print('Pop =',stack.pop(),'and Index =',stack.size())

if stack.isEmpty():
    print("Value in Stack = Empty")
else :
    print(stack)