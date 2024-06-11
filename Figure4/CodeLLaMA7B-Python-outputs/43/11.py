def pairs_sum_to_zero(l):
    
    # your code here
    # check if the list is empty
    if len(l) == 0:
        return False
    # check if there is a zero in the list
    if 0 in l:
        return True
    # check if there is a pair of distinct elements that sum to zero
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False


print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
