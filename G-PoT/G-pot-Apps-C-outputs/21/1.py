
def count_lucky_houses(L, R):
    mod = 10**9 + 7
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        num_6_8 = sum(1 for digit in num_str if digit in ['6', '8'])
        num_not_6_8 = len(num_str) - num_6_8
        if '4' not in num_str and num_6_8 == num_not_6_8:
            count += 1
    return count % mod

# Read input
L, R = map(int, input().split())

# Calculate and output result
print(count_lucky_houses(L, R))
