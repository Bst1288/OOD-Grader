'''
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 
โดยให้แสดงผลลัพธ์ตามตัวอย่าง

class Stack():
    def __init__(self, ls = None):
    def push(self,i):
    def pop(self):
    def isEmpty(self):
    def size(self):

def postFixeval(st):
    s = Stack()
    ### Enter Your Code Here ###
    return s.pop() 

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))
'''

class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def postFixeval(st):

    s = Stack()
    for opt in st:
        if opt == '+':
            object1 = s.pop()
            object2 = s.pop()
            object = float(object2) + float(object1)
            s.push(object)
        elif opt == '-':
            object1 = s.pop()
            object2 = s.pop()
            object = float(object2) - float(object1)
            s.push(object)
        elif opt == '*':
            object1 = s.pop()
            object2 = s.pop()
            object = float(object2) * float(object1)
            s.push(object)
        elif opt == '/':
            object1 = s.pop()
            object2 = s.pop()
            object = float(object2) / float(object1)
            s.push(object)
        else:
            s.push(opt) 

    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))