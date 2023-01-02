def bubbleSort(data, i, j, n):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return 
    if data[i] < data[j]:
        temp = data[j]
        data[j] = data[i]
        data[i] = temp
        bubbleSort(data, i, j+1, n);
    else:
        bubbleSort(data, i, j+1, n);
    return data

inp = [int(a) for a in input('Enter Input : ').split()]
print(bubbleSort(inp, 0, 0, len(inp)))