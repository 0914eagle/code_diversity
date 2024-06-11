def pairs_sum_to_zero(l):
    
    # Your code here
    # create a set of the list
    # iterate through the set
    # if the sum of two elements is zero, return True
    # else return False
    # O(n) time complexity
    # O(n) space complexity
    # set = set(l)
    # for i in set:
    #     if (i + i) in set:
    #         return True
    # return False

    # O(nlogn) time complexity
    # O(1) space complexity
    l.sort()
    for i in range(len(l) - 1):
        if l[i] + l[i + 1] == 0:
            return True
    return False


