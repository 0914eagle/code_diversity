
L, R = map(int, input().split())

def count_valid_houses(L, R):
    def is_valid(num):
        num_str = str(num)
        count_6_8 = sum(1 for digit in num_str if digit in ['6', '8'])
        count_not_6_8 = len(num_str) - count_6_8
        return '4' not in num_str and count_6_8 == count_not_6_8

    count = 0
    for num in range(L, R+1):
        if is_valid(num):
            count += 1

    return count % (10**9 + 7)

print(count_valid_houses(L, R))
