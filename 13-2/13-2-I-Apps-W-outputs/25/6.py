
def f1(n):
    # Calculate the minimum weight among all triangulations of the polygon
    return n * (n + 1) * (n + 2) // 6

def f2(n):
    # Calculate the minimum weight among all triangulations of the polygon
    return n * (n + 1) * (n + 2) // 6

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

