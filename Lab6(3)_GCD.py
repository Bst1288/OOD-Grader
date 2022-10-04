def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    #base case
    if a == b:
        return a
    if a>b:
        return gcd(a-b, b)
    return gcd(a, b-a)

a,b = map(int,input("Enter Input : ").split())
ans = gcd(a,b)
if(ans > 0 and a>b):
    print('The gcd of',a,'and',b,'is :',ans)
elif(ans > 0 and b>a):
    print('The gcd of',b,'and',a,'is :',ans)
else:
    print('Error! must be not all zero.')
