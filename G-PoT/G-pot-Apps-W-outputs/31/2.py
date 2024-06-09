
n = int(input())

def is_beautiful(num):
    k = num.bit_length() - 1
    beautiful_num = (2**k - 1) * (2**k - 1)
    if beautiful_num <= num:
        return beautiful_num
    else:
        return is_beautiful(beautiful_num)

print(is_beautiful(n))
