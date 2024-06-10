
def is_increasing(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def find_replacement(a, b):
    replaced = []
    for i in range(len(a)):
        if a[i] == 0:
            replaced.append(b[i])
    return replaced

def is_valid(a, b):
    replaced = find_replacement(a, b)
    return not is_increasing(replaced)

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes") if is_valid(a, b) else print("No")

if __name__ == '__main__':
    main()

