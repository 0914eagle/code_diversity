
def read_input():
    return map(int, input().split())

def count_pairs(L, R):
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if y % x == y ^ x:
                count += 1
    return count % (10**9 + 7)

def main():
    L, R = read_input()
    print(count_pairs(L, R))

if __name__ == '__main__':
    main()

