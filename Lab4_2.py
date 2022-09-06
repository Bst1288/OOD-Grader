'''
PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 
กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที 
(แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ
เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

Input :
EN <value>  เป็นโอตะธรรมดา  id = value
ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty
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
Q_en = Queue()
Q_es = Queue()

for l in S:
    temp = l.split()
    if temp[0] == 'EN':
        Q_en.enqueue(temp[1])
    elif temp[0] == 'ES':
        Q_es.enqueue(temp[1])
    elif temp[0] == 'D':
        if Q_es.size() != 0:
            temp = Q_es.dequeue()
            print(str(temp))
        elif Q_en.size() != 0:
            temp = Q_en.dequeue()
            print(str(temp))
        elif Q_en.size() == 0 and Q_es.size() == 0:
            print('Empty')