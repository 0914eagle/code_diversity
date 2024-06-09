
L, R = map(int, input().split())

def count_valid_houses(num):
    num_str = str(num)
    count_6_8 = 0
    count_other = 0
    for digit in num_str:
        if digit == '4':
            return False
        elif digit == '6' or digit == '8':
            count_6_8 += 1
        else:
            count_other += 1
    return count_6_8 == count_other

count = 0
for i in range(L, R+1):
    if count_valid_houses(i):
        count += 1

print(count % (10**9 + 7))
