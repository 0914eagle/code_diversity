
def f1(n):
    # Initialize a list to store the number of ways to fill
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        # Iterate over the previous ways and add the number of ways to fill the current row
        for j in range(i):
            ways[i] += ways[j]
    return ways[n]

def f2(n):
    # Initialize a list to store the number of ways to fill
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        # Iterate over the previous ways and add the number of ways to fill the current row
        for j in range(i):
            ways[i] += ways[j]
    return ways[n]

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

