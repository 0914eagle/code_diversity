
def f1(b, c):
    # Function to find the possible values of a and p
    # Given the arrays b and c
    n = len(b) + 1
    a = [0] * n
    p = [0] * n
    for i in range(n):
        # Find the minimum value in b and c
        min_b = min(b)
        min_c = min(c)
        # Find the index of the minimum value in b and c
        min_index_b = b.index(min_b)
        min_index_c = c.index(min_c)
        # Set the value of a and p based on the minimum indices
        a[i] = min_index_b + 1
        p[i] = min_index_c + 1
        # Remove the minimum values from b and c
        b.pop(min_index_b)
        c.pop(min_index_c)
    return a, p

def f2(b, c):
    # Function to check if the arrays b and c are valid
    # Given the arrays b and c
    n = len(b) + 1
    for i in range(n):
        # Check if the values in b are unique
        if b.count(i) != 1:
            return False
        # Check if the values in c are unique
        if c.count(i) != 1:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a, p = f1(b, c)
    if f2(b, c):
        print(*a)
    else:
        print(-1)

