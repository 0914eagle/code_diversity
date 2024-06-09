
def f1(n):
    # Initialize a list to store the number of ways to fill
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        # Loop through the possible values of j
        for j in range(i):
            # Calculate the number of ways to fill the ith row
            ways[i] += ways[j] * ways[i - j - 1]
    return ways[n]

def f2(n):
    # Initialize a list to store the number of ways to fill
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        # Loop through the possible values of j
        for j in range(i):
            # Calculate the number of ways to fill the ith row
            ways[i] += ways[j] * ways[i - j - 1]
    return ways[n]

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

