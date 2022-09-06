"""
จงเขียนฟังก์ชัน 
def odd_list(alist):
โดยมีการทำงานดังนี้
     # คืนlist ที่มีค่าเหมือนalist แต่มีเฉพาะตัวที่เป็นจำนวนคี่
     # เช่นalist = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]

โดยแก้ไขจากส่วนของคำสั่งต่อไปนี้


def odd_list(al):
    # เติมส่วนของคำสั่ง


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

"""

def odd_list(al):
    # เติมส่วนของคำสั่ง
    odd_num = []
    for num in al:
        if num % 2 == 1:
            odd_num.append(num)
    return odd_num


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
