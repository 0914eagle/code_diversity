
n = int(input())

def is_beautiful(num):
    k = num.bit_length() - 1
    beautiful_num = (2**k - 1) * (2**k - 1)
    return beautiful_num

for i in range(n, 0, -1):
    if n % i == 0 and is_beautiful(i) == i:
        print(i)
        break
