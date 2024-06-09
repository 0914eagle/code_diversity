
def f1(n, a):
    # Calculate the bitwise OR of all heights
    bitwise_or = 0
    for i in range(n):
        bitwise_or |= a[i]
    
    # Calculate the number of ways to choose two mountains
    ways = 0
    for i in range(n):
        for j in range(i+1, n):
            if bitwise_or > a[i] | a[j]:
                ways += 1
    
    return ways

def f2(n, a):
    # Calculate the bitwise OR of all heights
    bitwise_or = 0
    for i in range(n):
        bitwise_or |= a[i]
    
    # Calculate the number of ways to choose two mountains
    ways = 0
    for i in range(n):
        for j in range(i+1, n):
            if bitwise_or > a[i] | a[j]:
                ways += 1
    
    return ways

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

