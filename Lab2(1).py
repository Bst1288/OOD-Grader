'''
จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่
M=1000    CM=900    D=500    CD=400,
C=100    XC=90    L=50    XL=40,
X=10    IX=9    V=5    IV=4    I=1
เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I
(https://roman-numerals.info/)

class translator:
    def deciToRoman(self, num):
        ### Enter Your Code Here ###
    def romanToDeci(self, s):
        ### Enter Your Code Here ###
num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
'''
class translator:

    def deciToRoman(self, num):
        val = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        symbol = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]
        r = ''
        i = 0
        while  num > 0:
            for _ in range(num//val[i]):
                r += symbol[i]
                num -= val[i]
            i += 1
        return r


    def romanToDeci(self, s):
        tallies = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
        sum = 0
        for i in range(len(s) - 1):
            l = s[i]
            r = s[i + 1]
            if tallies[l] < tallies[r]:
                    sum -= tallies[l]
            else:
                sum += tallies[l]
        sum += tallies[s[-1]]
        return sum

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))