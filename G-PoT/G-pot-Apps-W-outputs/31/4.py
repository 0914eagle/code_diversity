
def greatest_beautiful_divisor(n):
    for k in range(1, 17):  # Iterate from 1 to 16 as 2^16 - 1 is the maximum beautiful number within the given constraints
        beautiful_num = (2**k - 1) * (2**k - 1)
        if n % beautiful_num == 0:
            return beautiful_num

n = int(input())
result = greatest_beautiful_divisor(n)
print(result)
