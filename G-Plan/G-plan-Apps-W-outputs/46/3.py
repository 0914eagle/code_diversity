
def can_split_cookies(A, B, C, D):
    total_sum = A + B + C + D
    if total_sum % 2 != 0:
        return "No"
    
    target_sum = total_sum // 2
    possible_sums = set()
    
    for subset in range(1, 1 << 4):
        subset_sum = 0
        for i in range(4):
            if subset & (1 << i):
                subset_sum += [A, B, C, D][i]
        possible_sums.add(subset_sum)
    
    if target_sum in possible_sums:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    print(can_split_cookies(A, B, C, D))