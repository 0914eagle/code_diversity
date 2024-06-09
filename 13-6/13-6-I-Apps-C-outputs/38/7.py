
def f(a):
    # Calculate the gcd of all the elements in the list
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd(gcd, a[i])
    return gcd

def f1(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()
    for i in range(n):
        for j in range(i, n):
            distinct_values.add(f(a[i:j+1]))
    return len(distinct_values)

def f2(n, a):
    # Initialize a dictionary to store the counts of each distinct value of f
    counts = {}
    for i in range(n):
        for j in range(i, n):
            value = f(a[i:j+1])
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
    return len(counts)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

