
def find_sub_rectangle(n, m, x, y, a, b):
    x1 = 0
    y1 = 0
    x2 = n
    y2 = m
    
    while x1 <= x and y1 <= y:
        if (x2 - x1) * b == (y2 - y1) * a:
            return x1, y1, x2, y2
        elif (x2 - x1) * b < (y2 - y1) * a:
            y1 += 1
        else:
            x1 += 1
    
    return -1, -1, -1, -1

def main():
    n, m, x, y, a, b = map(int, input().split())
    x1, y1, x2, y2 = find_sub_rectangle(n, m, x, y, a, b)
    print(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

