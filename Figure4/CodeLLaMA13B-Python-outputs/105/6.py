def by_length(arr):
    
    if len(arr) == 0:
        return []
    else:
        arr.sort()
        arr.reverse()
        arr = [str(i) for i in arr]
        arr = [i for i in arr if i in '123456789']
        arr = [i.replace('1', 'One') for i in arr]
        arr = [i.replace('2', 'Two') for i in arr]
        arr = [i.replace('3', 'Three') for i in arr]
        arr = [i.replace('4', 'Four') for i in arr]
        arr = [i.replace('5', 'Five') for i in arr]
        arr = [i.replace('6', 'Six') for i in arr]
        arr = [i.replace('7', 'Seven') for i in arr]
        arr = [i.replace('8', 'Eight') for i in arr]
        arr = [i.replace('9', 'Nine') for i in arr]
        return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
