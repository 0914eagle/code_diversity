
def count_lucky_houses(L, R):
    MOD = 10**9 + 7
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        if '4' in num_str:
            continue
        count_6_8 = sum(1 for digit in num_str if digit in ['6', '8'])
        count_not_6_8 = len(num_str) - count_6_8
        if count_6_8 == count_not_6_8:
            count += 1
    return count % MOD

# Input processing
L, R = map(int, input().split())

# Output
print(count_lucky_houses(L, R))
