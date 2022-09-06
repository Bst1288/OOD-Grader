"""

รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

BMI < 18.50 แสดงผล Less Weight

18.50 <= BMI  < 23 แสดงผล Normal Weight

23 <= BMI  < 25 แสดงผล Morethan Normal Weight

25 <= BMI  < 30 แสดงผล Getting Fat

BMI  >= 30 แสดงผล Fat

"""

try:
    h,w = list(map(float,input('Enter your High and Weight : ').split()))
    bmi = w/float(h*h)
    if(bmi<18.50):
        print('Less Weight')
    if(18.50<=bmi<23):
        print('Normal Weight')
    if(23<=bmi<25):
        print('More than Normal Weight')
    if(25<=bmi<30):
        print('Getting Fat')
    if(bmi>=30):
        print('Fat')
except ValueError:
        print('Plase enter your High and Weight')