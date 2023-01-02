def get_maxIndex(l):
    maxInx = len(l)-1
    if l[maxInx] != max(l) and maxInx - 1 >= 0:
        return get_maxIndex(l[:maxInx])
    else:
        return maxInx

def stright_selection_sort(l, right = None):
    if right == None:
        right = len(l)-1
    if right < 0:
        return l

    maxInx = get_maxIndex(l[:right + 1])
    if maxInx != right:
        l[right],l[maxInx] = l[maxInx],l[right]
        print(f'swap {l[maxInx]} <-> {l[right]} : {l}')
    return stright_selection_sort(l, right-1)

inp = list(map(int, input('Enter Input : ').split()))
ans = stright_selection_sort(inp)
print(inp)