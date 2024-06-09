
def f1(S, x1, y1, x2, y2):
    # Find the line that passes through the two points
    m = (y2-y1)/(x2-x1)
    b = y1 - m*x1
    
    # Check if the line intersects with any of the other lines
    for i in range(S):
        x3, y3, x4, y4 = map(int, input().split())
        if x3 == x4:
            continue
        m2 = (y4-y3)/(x4-x3)
        b2 = y3 - m2*x3
        if m == m2:
            continue
        x = (b2-b)/(m-m2)
        if x >= 0 and x <= 10000:
            return "different"
    return "same"

def f2(S, x1, y1, x2, y2):
    # Find the line that passes through the two points
    m = (y2-y1)/(x2-x1)
    b = y1 - m*x1
    
    # Check if the line intersects with any of the other lines
    for i in range(S):
        x3, y3, x4, y4 = map(int, input().split())
        if x3 == x4:
            continue
        m2 = (y4-y3)/(x4-x3)
        b2 = y3 - m2*x3
        if m == m2:
            continue
        x = (b2-b)/(m-m2)
        if x >= 0 and x <= 10000:
            return "different"
    return "same"

if __name__ == '__main__':
    S = int(input())
    for i in range(S):
        x1, y1, x2, y2 = map(int, input().split())
        print(f1(S, x1, y1, x2, y2))
    T = int(input())
    for i in range(T):
        x3, y3, x4, y4 = map(int, input().split())
        print(f2(S, x3, y3, x4, y4))

