'''
จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
'''

def ManageStack(stack):
    ls = []
    def isA(ls,i):
        ls.append(i)
        print('Add = ' + str(i))

    def isP(ls):
        if len(ls) == 0:
            print('-1')
        else:
            temp = ls[-1]
            ls.pop()
            print('Pop = ' + str(temp))

    def isD(ls,temp):
        num = 0

        if len(ls) == 0:
            print('-1')
        else:
            for i in ls:
                if i == temp:
                    num += 1
            for i in range(num):
                ls.remove(temp)
                print('Delete =', str(temp))
        
    def isLD(ls,temp):
        ls_temp = []

        if len(ls) == 0:
            print('-1')
        else:
            for i in range(len(ls)-1,-1,-1):
                if int(ls[i]) >= int(temp):
                    ls_temp.append(ls[i])
                else:
                    print('Delete = ' + str(ls[i]) + ' Because ' + str(ls[i]) + ' is less than ' + str(temp))
        ls_temp.reverse()
        return ls_temp

    def isMD(ls,temp):
        ls_temp = []
        
        if len(ls) == 0:
            print('-1')
        else:
            for i in range(len(ls)-1,-1,-1):
                if int(ls[i]) <= int(temp):
                    ls_temp.append(ls[i])
                else:
                    print('Delete = ' + str(ls[i]) +" Because " + str(ls[i]) + " is more than " + str(temp))
        ls_temp.reverse()
        return ls_temp
    
    for i in stack:
        s = i.split()
        if s[0] == 'A':
            isA(ls,s[1])
        elif s[0] == 'P':
            isP(ls)
        elif s[0] == 'D':
            isD(ls,s[1])
        elif s[0] == 'LD':
            ls = isLD(ls,s[1])
        elif s[0] == 'MD':
            ls = isMD(ls,s[1])
    for i in range(0, len(ls)):
        ls[i] = int(ls[i])
    print('Value in Stack = ' + str(ls))
    
inp = input('Enter Input : ').split(',')
ManageStack(inp)

