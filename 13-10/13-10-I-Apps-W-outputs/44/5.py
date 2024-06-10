
def read_input():
    return map(int, input().split())

def get_xor(a, b):
    return a ^ b

def get_pair_count(l, r):
    count = 0
    for x in range(l, r+1):
        for y in range(x, r+1):
            if get_xor(x, y) == y:
                count += 1
    return count % 1000000007

def main():
    l, r = read_input()
    print(get_pair_count(l, r))

if __name__ == '__main__':
    main()

