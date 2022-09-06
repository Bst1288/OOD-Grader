'''
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้
    1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
จะไม่สามารถพูดว่า “Apple” ได้อีก
    2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที
    3. Ignore Case Sensitive

โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
- P < word > จะเป็นการต่อคำ
- R จะเป็นการเริ่มคำใหม่ทั้งหมด
- X เป็นการระบุว่าจบการทำงาน
โดยจะรับประกันว่า word ที่รับมา จะมีความยาวอย่างน้อยที่สุดคือ
'''

print("*** TorKham HanSaa ***")
input = input("Enter Input : ").split(",")

now = []
previous = ""

for element in input :
    if element == "X" :
        break
    elif element == "R" :
        now.clear()
        previous = ""
        print("game restarted")
    else :
        temp = element.split(" ")
        if temp[0] == "P" :
            cmp1 = temp[1][:2].lower()
            cmp2 = previous[-2:].lower()

            if ( cmp1 == cmp2 and previous != "" ):
                now.append(temp[1])
                previous = temp[1]
                print("'" + temp[1] + "'" + " -> ",end="")
                print(now)
            elif ( cmp1 != cmp2 and previous == "") :
                now.append(temp[1])
                previous = temp[1]
                print("'" + temp[1] + "'" + " -> ",end="")
                print(now)
            else :
                print("'" + temp[1] + "'" + " -> game over")
                break
        else :
            print("'" + element + "'" + " is Invalid Input !!!")
            break