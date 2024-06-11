def by_length(arr):
    
    # YOUR CODE HERE
    arr.sort()
    arr.reverse()
    arr = [str(x) for x in arr]
    arr = [x.replace('1', 'One') for x in arr]
    arr = [x.replace('2', 'Two') for x in arr]
    arr = [x.replace('3', 'Three') for x in arr]
    arr = [x.replace('4', 'Four') for x in arr]
    arr = [x.replace('5', 'Five') for x in arr]
    arr = [x.replace('6', 'Six') for x in arr]
    arr = [x.replace('7', 'Seven') for x in arr]
    arr = [x.replace('8', 'Eight') for x in arr]
    arr = [x.replace('9', 'Nine') for x in arr]
    return arr

#