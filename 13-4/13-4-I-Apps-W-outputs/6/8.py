
def get_max_sum(k_2, k_3, k_5, k_6):
    max_sum = 0
    for i in range(k_2 + 1):
        for j in range(k_3 + 1):
            for k in range(k_5 + 1):
                for l in range(k_6 + 1):
                    sum = 256 * i + 32 * j
                    if sum > max_sum:
                        max_sum = sum
    return max_sum

