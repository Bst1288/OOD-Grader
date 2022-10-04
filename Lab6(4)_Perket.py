S = list()
B = list()
Sol = list()

def perket(i, num, sour, bitt):
    if i == len(inp):
        if num != 0:
            Sol.append(abs(bitt -  sour))
        return
    perket(i+1, num, sour, bitt)
    perket(i+1, num+1, sour*int(S[i]), bitt+int(B[i]))

inp = input('Enter Input : ').split(',')

for i in inp:
    s, b = i.split(' ')
    S.append(s)
    B.append(b)

perket(0, 0, 1, 0)
print(min(Sol))