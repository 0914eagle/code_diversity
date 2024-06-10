
def get_remainder(x, y):
    return y % x

def get_xor(a, b):
    return a ^ b

def count_pairs(L, R):
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if get_remainder(x, y) == get_xor(x, y):
                count += 1
    return count % (10**9 + 7)

if __name__ == '__main__':
    L, R = map(int, input().split())
    print(count_pairs(L, R))

