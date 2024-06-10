
def find_pairs(L, R):
    count = 0
    for x in range(L, R + 1):
        for y in range(x, R + 1):
            if (y ^ x) % 1000000007 == y % 1000000007:
                count += 1
    return count

def main():
    L, R = map(int, input().split())
    print(find_pairs(L, R))

if __name__ == '__main__':
    main()

