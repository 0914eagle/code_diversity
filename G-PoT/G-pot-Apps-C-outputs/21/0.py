
def count_lucky_houses(L, R):
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        count_6_8 = num_str.count('6') + num_str.count('8')
        count_not_6_8 = len(num_str) - count_6_8
        if '4' not in num_str and count_6_8 == count_not_6_8:
            count += 1
    return count % (10**9 + 7)

# Input
L, R = map(int, input().split())

# Output
print(count_lucky_houses(L, R))
