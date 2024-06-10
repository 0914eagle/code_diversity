
def get_xor_sum(a, l, r):
    return sum(a[l:r+1])

def get_xor_pair_count(a):
    n = len(a)
    count = 0
    for l in range(n):
        for r in range(l, n):
            if get_xor_sum(a, l, r) == get_xor_sum(a, 0, r):
                count += 1
    return count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_xor_pair_count(a))

if __name__ == '__main__':
    main()

