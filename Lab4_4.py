'''
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                   0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                  1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                  3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย
กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,
เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
    วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่       +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                 - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน
โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่
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
        return self.items[0]

myQ = Queue()
yourQ = Queue()

myList = []
yourList = []

input = str(input('Enter Input : ')).split(',')
for i in input:
    my_str,your_str = i.split(' ')
    myQ.enqueue(my_str)
    yourQ.enqueue(your_str)
    myList.append(my_str)
    yourList.append(your_str)

print('My   Queue = ',end='')
for i in range(len(myList)):
    print(myList[i],end='')
    if i != len(myList)-1:
        print(', ',end='')

print('')
print('Your Queue = ',end='')
for i in range(len(yourList)):
    print(yourList[i],end='')
    if i != len(myList)-1:
        print(', ',end='')

print('')
print('My   Activity:Location = ',end='')
for i in range(len(myList)):
    myAct, myLoc = str(myList[i]).split(':')
    if myAct == '0':
        print('Eat:',end='')
    elif myAct == '1':
        print('Game:',end='')
    elif myAct == '2':
        print('Learn:',end='')
    elif myAct == '3':
        print('Movie:',end='')

    if myLoc == '0':
        print('Res.',end='')
    elif myLoc == '1':
        print('ClassR.',end='')
    elif myLoc == '2':
        print('SuperM.',end='')
    elif myLoc == '3':
        print('Home',end='')

    if i != len(myList)-1:
        print(', ',end='')
    else:
        print('')

print('Your Activity:Location = ',end='')
for i in range(len(yourList)):
    yourAct, yourLoc = str(yourList[i]).split(':')
    if yourAct == '0':
        print('Eat:',end='')
    elif yourAct == '1':
        print('Game:',end='')
    elif yourAct == '2':
        print('Learn:',end='')
    elif yourAct == '3':
        print('Movie:',end='')

    if yourLoc == '0':
        print('Res.',end='')
    elif yourLoc == '1':
        print('ClassR.',end='')
    elif yourLoc == '2':
        print('SuperM.',end='')
    elif yourLoc == '3':
        print('Home',end='')
        
    if i != len(yourList)-1:
        print(', ',end='')
    else:
        print('')

s = 0
while myQ.isEmpty() != True and yourQ.isEmpty() != True:
    myAct, myLoc = str(myQ.peek()).split(':')
    yourAct, yourLoc = str(yourQ.peek()).split(':')

    if myAct == yourAct and myLoc != yourLoc:
        s = s+1
    elif myAct != yourAct and myLoc == yourLoc:
        s = s+2
    elif myAct == yourAct and myLoc == yourLoc:
        s = s+4
    elif myAct != yourAct and myLoc != yourLoc:
        s = s-5
    myQ.dequeue()
    yourQ.dequeue()

score = str(s)
if s >= 7:
    print("Yes! You're my love! : Score is ",end='')
    print(score,end='')
    print('.')
elif s < 7 and s > 0:
    print("Umm.. It's complicated relationship! : Score is ",end='')
    print(score,end='')
    print('.')
else:
    print("No! We're just friends. : Score is ",end='')
    print(score,end='')
    print('.')