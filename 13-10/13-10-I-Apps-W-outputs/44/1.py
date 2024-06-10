
def xor(a, b):
    return a ^ b

def solve(L, R):
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if xor(x, y) == y:
                count += 1
    return count % 1000000007

def main():
    L, R = map(int, input().split())
    print(solve(L, R))

if __name__ == '__main__':
    main()

