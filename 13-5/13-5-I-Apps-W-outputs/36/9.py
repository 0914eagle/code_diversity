
def f1(n, a):
    # Calculate the bitwise OR of all the heights
    or_heights = 0
    for i in range(n):
        or_heights |= a[i]
    
    # Calculate the number of ways to choose two mountains
    num_ways = 0
    for i in range(n):
        for j in range(i+1, n):
            if or_heights | a[i] | a[j] > a[i] | a[j]:
                num_ways += 1
    
    return num_ways

def f2(n, a):
    # Calculate the bitwise OR of all the heights
    or_heights = 0
    for i in range(n):
        or_heights |= a[i]
    
    # Calculate the number of ways to choose two mountains
    num_ways = 0
    for i in range(n):
        for j in range(i+1, n):
            if or_heights | a[i] | a[j] > a[i] | a[j]:
                num_ways += 1
    
    return num_ways

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

