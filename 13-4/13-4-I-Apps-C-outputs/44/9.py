
def find_rectangle(n, m, x, y, a, b):
    x1 = 0
    y1 = 0
    x2 = n
    y2 = m
    
    while x1 <= x and y1 <= y:
        if x2 - x1 == a and y2 - y1 == b:
            return [x1, y1, x2, y2]
        if x2 - x1 > a:
            x2 -= 1
        if y2 - y1 > b:
            y2 -= 1
        if x2 - x1 < a:
            x1 += 1
        if y2 - y1 < b:
            y1 += 1
    
    return []

def main():
    n, m, x, y, a, b = map(int, input().split())
    print(find_rectangle(n, m, x, y, a, b))

if __name__ == '__main__':
    main()

