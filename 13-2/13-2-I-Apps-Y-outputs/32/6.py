
def can_reach_destination(start, end, charge):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return charge >= 0
    if abs(dx) > abs(dy):
        if dx < 0:
            return can_reach_destination((x1+1, y1), end, charge-1)
        else:
            return can_reach_destination((x1-1, y1), end, charge-1)
    else:
        if dy < 0:
            return can_reach_destination(start, (x1, y1+1), charge-1)
        else:
            return can_reach_destination(start, (x1, y1-1), charge-1)

def main():
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    charge = int(input())
    print("Y" if can_reach_destination(start, end, charge) else "N")

if __name__ == "__main__":
    main()

