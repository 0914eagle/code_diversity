
def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, k, a, b

def is_increasing(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            return False
    return True

def replace_zeros(n, k, a, b):
    replaced = False
    for i in range(n):
        if a[i] == 0:
            replaced = True
            a[i] = b.pop(0)
    return replaced

def main():
    n, k, a, b = get_input()
    replaced = replace_zeros(n, k, a, b)
    if replaced and not is_increasing(a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

