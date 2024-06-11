def by_length(arr):
    
    if len(arr) == 0:
        return []
    else:
        arr.sort()
        arr.reverse()
        arr = [str(i) for i in arr]
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


