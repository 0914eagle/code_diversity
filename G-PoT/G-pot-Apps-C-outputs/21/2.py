
def count_lucky_houses(L, R):
    count = 0
    for house_num in range(L, R+1):
        num_str = str(house_num)
        count_6_8 = 0
        count_other = 0
        for digit in num_str:
            if digit == '4':
                break
            elif digit == '6' or digit == '8':
                count_6_8 += 1
            else:
                count_other += 1
        if count_6_8 == count_other:
            count += 1
    return count % (10**9 + 7)

# Input
L, R = map(int, input().split())

# Output
print(count_lucky_houses(L, R))
