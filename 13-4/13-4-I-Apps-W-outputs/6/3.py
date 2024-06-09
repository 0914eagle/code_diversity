
def get_max_sum(k_2, k_3, k_5, k_6):
    max_sum = 0
    for i in range(k_2+1):
        for j in range(k_3+1):
            for k in range(k_5+1):
                for l in range(k_6+1):
                    sum = i*2 + j*3 + k*5 + l*6
                    max_sum = max(max_sum, sum)
    return max_sum

