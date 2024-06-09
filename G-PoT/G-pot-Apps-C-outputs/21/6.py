
def count_lucky_houses(L, R):
    mod = 10**9 + 7
    count = 0
    
    for num in range(L, R+1):
        num_str = str(num)
        count_6_8 = 0
        count_other = 0
        
        for digit in num_str:
            if digit == '4':
                break
            elif digit in ['6', '8']:
                count_6_8 += 1
            else:
                count_other += 1
        
        if count_6_8 == count_other:
            count += 1
    
    return count % mod

# Input
L, R = map(int, input().split())

# Output
print(count_lucky_houses(L, R))
