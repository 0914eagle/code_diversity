
def get_pairs(L, R):
    count = 0
    for x in range(L, R+1):
        for y in range(x, R+1):
            if (y ^ x) == y:
                count += 1
    return count

def main():
    L, R = map(int, input().split())
    print(get_pairs(L, R))

if __name__ == '__main__':
    main()

