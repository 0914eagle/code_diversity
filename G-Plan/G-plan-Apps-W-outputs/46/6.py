
def is_possible_to_split_cookies(A, B, C, D):
    total_sum = A + B + C + D
    if total_sum % 2 != 0:
        return "No"
    
    half_sum = total_sum // 2
    for mask in range(1, 1 << 4):
        sum_subset = 0
        for i in range(4):
            if mask & (1 << i):
                sum_subset += [A, B, C, D][i]
        if sum_subset == half_sum:
            return "Yes"
    
    return "No"

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    print(is_possible_to_split_cookies(A, B, C, D))
