
def get_xor(x, y):
    return x ^ y

def count_pairs(L, R):
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if get_xor(x, y) == y:
                count += 1
    return count % 1000000007

if __name__ == '__main__':
    L, R = map(int, input().split())
    print(count_pairs(L, R))

