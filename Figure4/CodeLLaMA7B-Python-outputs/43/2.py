def pairs_sum_to_zero(l):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False
    # O(n^2) solution

    # O(n) solution
    # create a set of the list
    # for each element in the list, check if -element exists in the set
    # if it does, return True
    # return False
    s = set(l)
    for i in l:
        if -i in s:
            return True
    return False


print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
