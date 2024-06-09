
def is_pythagorean_triple(a, b, c):
    return a*a + b*b == c*c

def find_pythagorean_triple(n):
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = n**2 - a**2 - b**2
            if c >= 0 and is_pythagorean_triple(a, b, c):
                return a, b, c
    return -1, -1, -1

if __name__ == '__main__':
    n = int(input())
    a, b, c = find_pythagorean_triple(n)
    if a == -1:
        print(-1)
    else:
        print(a, b, c)

