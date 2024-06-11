def pairs_sum_to_zero(l):
    
    # Your code here
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False
    return any(l[i] + l[j] == 0 for i in range(len(l)) for j in range(i+1, len(l)))


