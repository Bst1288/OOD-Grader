"""
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา 
โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

"""
print("*** Fun with countdown ***")
lst = list(map(int, input("Enter List : ").split()))
i = len(lst)-1
index = []
while i > 0 or i == 0:
    if lst[i] == 1:
        x = i
        temp = []
        temp.append(lst[x])
        while lst[x-1]-lst[x] == 1:
            temp.append(lst[x-1])
            x = x-1
            if x <= 0:
                break
        temp.sort(reverse=True)
        index.append(temp)
        i = x
    i = i-1
index.reverse()
print("[{0}, {1}]".format(len(index),index))
