
def get_min_c(a, b):
    # Calculate the bitwise AND of a and b
    c = a & b
    # Return the minimum value of c
    return c.min()

def get_min_c_or(a, b):
    # Calculate the bitwise AND of a and b
    c = a & b
    # Calculate the bitwise OR of c
    c_or = c.sum(axis=1)
    # Return the minimum value of c_or
    return c_or.min()

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_min_c_or(a, b))

