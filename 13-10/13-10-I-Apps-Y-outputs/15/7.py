
def get_x(p1, p2, ..., pn):
    x = 0
    for i in range(n):
        x += p[i] ** (i+1)
    return x

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    print(get_x(p[0], p[1], ..., p[n-1]))

if __name__ == '__main__':
    main()

