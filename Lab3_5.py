'''
จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง
class Stack :
    ### Enter Your Code Here ###

def dec2bin(decnum):
    s = Stack()
    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))
'''

class Stack :
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def dec2bin(decnum):
    
    i = 0
    s = Stack()
    while 2**i<=decnum:
        i += 1
    n = i-1
    while n >= 0:
        if decnum >= 2**n:
            decnum -= 2**n
            s.push(1)
        else:
            s.push(0)
        n = n-1
    s.items.reverse()
    value = ""
    while s.size() > 0:
        value += str(s.peek())
        s.pop()
    return value


print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))