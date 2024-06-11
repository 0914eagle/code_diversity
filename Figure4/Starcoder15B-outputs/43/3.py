def pairs_sum_to_zero(l):
    
    # Your code here
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == 0:
                return True
    return False


