
def find_beautiful_divisor(n):
    for k in range(1, 18):  # Maximum k for n <= 10^5 is 17
        beautiful_num = (2**k - 1) * (2**k - 1)
        if n % beautiful_num == 0:
            return beautiful_num

n = int(input())
result = find_beautiful_divisor(n)
print(result)
