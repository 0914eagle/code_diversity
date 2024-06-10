
def is_possible_to_split_cookies(A, B, C, D):
    total_sum = A + B + C + D
    if total_sum % 2 != 0:
        return "No"
    
    target_sum = total_sum // 2
    for mask in range(1, 1 << 4):
        current_sum = 0
        for i in range(4):
            if (mask >> i) & 1:
                current_sum += [A, B, C, D][i]
        if current_sum == target_sum:
            return "Yes"
    
    return "No"

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    print(is_possible_to_split_cookies(A, B, C, D))
