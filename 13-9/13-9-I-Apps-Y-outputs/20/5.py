
def find_min_n(l, d, x):
    for n in range(l, d+1):
        if sum(int(i) for i in str(n)) == x:
            return n
    return -1

def find_max_m(l, d, x):
    for m in range(l, d+1):
        if sum(int(i) for i in str(m)) == x:
            return m
    return -1

if __name__ == '__main__':
    l = int(input())
    d = int(input())
    x = int(input())
    print(find_min_n(l, d, x))
    print(find_max_m(l, d, x))

