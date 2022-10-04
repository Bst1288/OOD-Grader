def asteroid_collision(asts):
    ls = []
    def checkCollision(ls,asts):
        if len(ls) == 0:
            ls.append(asts)
        elif asts < 0 and ls[-1] > 0:
            if asts + ls[-1] == 0:
                ls.pop()
            elif asts + ls[-1] < 0:
                ls.pop()
                checkCollision(ls,asts)
        else:
            ls.append(asts)
    
    def recursiveLoop (i,ls,asts):
        if i != len(asts):
            checkCollision(ls,asts[i])
            recursiveLoop(i+1,ls,asts)

    recursiveLoop(0,ls,asts)

    return ls

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))