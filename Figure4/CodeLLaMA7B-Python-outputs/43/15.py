def pairs_sum_to_zero(l):
    
    # Your code here
    # create a dictionary with the values as keys
    # if the sum of two keys is 0, return True
    # otherwise return False
    # O(n) time and space
    # O(n) space
    d = {}
    for i in l:
        if i in d:
            return True
        else:
            d[i] = 1
    return False


