
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

def find_matching_statue(b, empty_island):
    for i in range(len(b)):
        if b[i] == empty_island:
            return i
    return -1

def can_rearrange(n, a, b):
    empty_island = find_empty_island(a)
    if empty_island == -1:
        return False
    matching_statue = find_matching_statue(b, empty_island)
    if matching_statue == -1:
        return False
    a[empty_island] = b[matching_statue]
    b[matching_statue] = 0
    return can_rearrange(n, a, b)

def main():
    n, a, b = get_input()
    if can_rearrange(n, a, b):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

