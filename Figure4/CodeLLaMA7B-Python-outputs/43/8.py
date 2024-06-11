def pairs_sum_to_zero(l):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # # or
    # # create a set of the list
    # s = set(l)
    # # iterate through the set
    # for i in s:
    #     if -i in s:
    #         return True
    # return False

    # # or
    # # create a set of the list
    # s = set(l)
    # # iterate through the set
    # for i in s:
    #     if -i in s and i != -i:
    #         return True
    # return False

    # or
    # create a set of the list
    s = set(l)
    # iterate through the set
    for i in s:
        if -i in s:
            return True
    return False


print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
