
def get_min_time(x1, y1, x2, y2, n, m, l, e, v):
    # Base case: if x1 and x2 are on the same floor, return the absolute difference between y1 and y2
    if x1 == x2:
        return abs(y1 - y2)
    
    # Initialize the minimum time to travel from x1, y1 to x2, y2 as infinity
    min_time = float('inf')
    
    # If x1 and x2 are not on the same floor, we need to use the elevator or the stairs
    # Iterate over all floors between x1 and x2 (both inclusive)
    for i in range(min(x1, x2), max(x1, x2) + 1):
        # If i is not the current floor, we need to use the stairs or the elevator to get to i
        if i != x1:
            # If i is a stair floor, we need to use the stairs to get to i
            if i in l:
                min_time = min(min_time, get_min_time(x1, y1, i, y1, n, m, l, e, v) + get_min_time(i, y1, i, y2, n, m, l, e, v))
            # If i is an elevator floor, we need to use the elevator to get to i
            elif i in e:
                min_time = min(min_time, get_min_time(x1, y1, i, y1, n, m, l, e, v) + get_min_time(i, y1, i, y2, n, m, l, e, v))
    
    return min_time

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    l = set(map(int, input().split()))
    e = set(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(get_min_time(x1, y1, x2, y2, n, m, l, e, v))

if __name__ == '__main__':
    main()

