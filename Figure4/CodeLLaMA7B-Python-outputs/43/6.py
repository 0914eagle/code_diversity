def pairs_sum_to_zero(l):
    
    # Your code here
    # create a dictionary with the values as keys
    # iterate through the dictionary and check if the value - key exists
    # if it does, return True
    # if it doesn't, return False
    # if the list is empty, return False
    # if the list has only one element, return False
    # if the list has two elements, check if they are equal
    # if they are, return False
    # if they are not, check if the sum of the two elements is zero
    # if it is, return True
    # if it is not, return False
    if len(l) == 0:
        return False
    elif len(l) == 1:
        return False
    elif len(l) == 2:
        if l[0] == l[1]:
            return False
        else:
            if l[0] + l[1] == 0:
                return True
            else:
                return False
    else:
        d = {}
        for i in l:
            d[i] = 1
        for i in l:
            if d.get(i) != None:
                if i + (i * -1) == 0:
                    return True
        return False


print(pairs_sum_to_zero([1, 2, 3, 7]))
