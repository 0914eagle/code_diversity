
def get_input():
    N = int(input())
    p = list(map(int, input().split()))
    return N, p

def is_sorted(p):
    return all(p[i] < p[i+1] for i in range(len(p)-1))

def swap(p, i, j):
    p[i], p[j] = p[j], p[i]

def can_sort(p):
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                swap(p, i, j)
                if is_sorted(p):
                    return True
                swap(p, i, j)
    return False

def main():
    N, p = get_input()
    print("YES") if can_sort(p) else print("NO")

if __name__ == '__main__':
    main()

