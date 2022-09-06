'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา
E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป
D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue
                    หลังจากทำการ dequeue แล้ว
*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***
'''
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

S = input('Enter Input : ').split(',')
Q = Queue()
for symbol in S:
    if symbol[0] == "E":
        int,temp = symbol.split()
        Q.enqueue(temp)
        print('Add' , Q.peek() , 'index is' , Q.size()-1)

    elif symbol[0] == 'D':
        if Q.isEmpty():
            print('-1')
        else:
            print('Pop', Q.dequeue(),'size in queue is', Q.size())

if Q.isEmpty():
    print("Empty")
else :
    print('Number in Queue is : ',Q.items)


