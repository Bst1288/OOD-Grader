def max(l):
    if len(l) == 1:
        return l[0]
    else:
        m = max(l[1:])
        if m > l[0]:
            return m
        else:
            return l[0]

inp = list(map(int,input('Enter Input : ').strip().split()))
print('Max : ',end='')
print(max(inp))