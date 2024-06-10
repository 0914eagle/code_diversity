
def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def get_detachment(a, k):
    n = len(a)
    detachment = []
    for i in range(k):
        c = 1
        p = []
        while c <= n:
            p.append(a[i % n])
            i += 1
            c += 1
        detachment.append((c, p))
    return detachment

def print_output(detachment):
    for c, p in detachment:
        print(c, *p)

def main():
    n, k, a = get_input()
    detachment = get_detachment(a, k)
    print_output(detachment)

if __name__ == '__main__':
    main()

