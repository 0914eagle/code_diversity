
def find_beautiful_divisor(n):
    for k in range(1, 18):  # 18 is chosen because 2^18 - 1 = 262143 > 10^5
        beautiful_num = (2**k - 1) * (2**k - 1)
        if n % beautiful_num == 0:
            return beautiful_num

n = int(input())
result = find_beautiful_divisor(n)
print(result)
