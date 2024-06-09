
def get_max_sum(k2, k3, k5, k6):
    max_sum = 0
    for i in range(k2+1):
        for j in range(k3+1):
            for k in range(k5+1):
                for l in range(k6+1):
                    sum = i*2 + j*3 + k*5 + l*6
                    max_sum = max(max_sum, sum)
    return max_sum

