
n = int(input())

def is_beautiful(num):
    k = num.bit_length() - 1
    return num == ((1 << k) - 1) * ((1 << k) - 1)

for i in range(n, 0, -1):
    if n % i == 0 and is_beautiful(i):
        print(i)
        break
