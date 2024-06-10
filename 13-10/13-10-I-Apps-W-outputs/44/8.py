
def mod_pow(base, exponent, modulus):
    if exponent == 0:
        return 1
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def get_xor_value(x, y):
    xor_value = 0
    while x > 0 and y > 0:
        if x % 2 == 1 and y % 2 == 1:
            xor_value += 1
        x //= 2
        y //= 2
    return xor_value

def count_pairs(l, r):
    count = 0
    for x in range(l, r + 1):
        for y in range(x, r + 1):
            if get_xor_value(x, y) == y ^ x:
                count += 1
    return count

def main():
    l, r = map(int, input().split())
    print(count_pairs(l, r))

if __name__ == '__main__':
    main()

