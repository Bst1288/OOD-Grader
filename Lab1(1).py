"""
เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล
"""
PI = 3.141592653589793
r = float(input("r="))
area = PI*(r*r)
print("Area=",area,sep='')