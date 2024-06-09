
def f1(n):
    # Base case: if n is 1, there is only one way to fill the tiles
    if n == 1:
        return 1
    
    # Recursive case: fill the tiles with the given shape
    # and count the number of ways to fill the remaining tiles
    count = 0
    for i in range(n):
        count += f1(n-i)
    return count

def f2(n):
    # Base case: if n is 1, there is only one way to fill the tiles
    if n == 1:
        return 1
    
    # Recursive case: fill the tiles with the given shape
    # and count the number of ways to fill the remaining tiles
    count = 0
    for i in range(n):
        count += f2(n-i)
    return count

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

