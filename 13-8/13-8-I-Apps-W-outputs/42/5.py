
def get_swap_count(n, a, p):
    # Count the number of leaves
    leaves = []
    for i in range(1, n+1):
        if p[i] == 0:
            leaves.append(i)
    
    # Count the number of ways to make the swap
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and a[i] != a[j] and leaves.count(i) == 1 and leaves.count(j) == 1:
                count += 1
    
    return count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_swap_count(n, a, p))

if __name__ == '__main__':
    main()

