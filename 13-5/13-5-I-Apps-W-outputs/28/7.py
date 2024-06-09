
def f1(n):
    # Calculate the number of ways to fill the tiles
    num_ways = 0
    
    # Iterate through all possible combinations of shapes
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # Check if the current combination is valid
                if i + j + k == n:
                    num_ways += 1
    
    return num_ways

def f2(n):
    # Calculate the number of ways to fill the tiles using a recursive approach
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f2(n - 1) + f2(n - 2) + f2(n - 3)

if __name__ == '__main__':
    n = int(input())
    print(f1(n))
    print(f2(n))

