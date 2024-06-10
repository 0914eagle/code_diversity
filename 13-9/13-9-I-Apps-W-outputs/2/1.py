
def get_triangle_points(n, m, k):
    for x1 in range(n+1):
        for y1 in range(m+1):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    for x3 in range(x2+1, n+1):
                        for y3 in range(y2+1, m+1):
                            if (x1*y2 + x2*y3 + x3*y1) % k == 0:
                                return "YES\n" + str(x1) + " " + str(y1) + "\n" + str(x2) + " " + str(y2) + "\n" + str(x3) + " " + str(y3)
    return "NO"

def main():
    n, m, k = map(int, input().split())
    print(get_triangle_points(n, m, k))

if __name__ == '__main__':
    main()

