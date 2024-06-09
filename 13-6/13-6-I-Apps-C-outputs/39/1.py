
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, a, b

def find_empty_island(a):
    for i in range(len(a)):
        if a[i] == 0:
            return i
    return -1

def find_statue(a, b, empty_island):
    for i in range(len(a)):
        if a[i] != 0 and b[i] != 0 and a[i] != b[i]:
            return i
    return -1

def can_rearrange(n, a, b):
    empty_island = find_empty_island(a)
    if empty_island == -1:
        return "NO"
    statue = find_statue(a, b, empty_island)
    if statue == -1:
        return "NO"
    return "YES"

def main():
    n, a, b = get_input()
    print(can_rearrange(n, a, b))

if __name__ == '__main__':
    main()

