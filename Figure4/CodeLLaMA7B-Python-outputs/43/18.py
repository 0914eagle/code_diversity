def pairs_sum_to_zero(l):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # # or
    # # using set
    # s = set(l)
    # for i in s:
    #     if -i in s:
    #         return True
    # return False

    # # or
    # # using dictionary
    # d = {}
    # for i in l:
    #     if i in d:
    #         return True
    #     else:
    #         d[i*-1] = i
    # return False

    # or
    # using set
    s = set(l)
    return any(i + i2 == 0 for i in s for i2 in s)


print(pairs_sum_to_zero([1, 3, 5, 0]))
print(pairs_sum_to_zero([1, 3, -2, 1]))
print(pairs_sum_to_zero([1, 2, 3, 7]))
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
print(pairs_sum_to_zero([1]))
