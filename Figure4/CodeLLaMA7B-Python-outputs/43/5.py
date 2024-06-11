def pairs_sum_to_zero(l):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # using set
    # s = set(l)
    # for i in s:
    #     if -i in s:
    #         return True
    # return False

    # using dictionary
    d = {}
    for i in l:
        if -i in d:
            return True
        else:
            d[i] = True
    return False


print(pairs_sum_to_zero([1, 2, 3, 7]))
