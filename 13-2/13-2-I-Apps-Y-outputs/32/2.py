
def can_reach_destination(start, end, charge):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return charge >= 0
    if abs(dx) > abs(dy):
        if dx < 0:
            dx, dy = -dx, -dy
        if dy < 0:
            dy = -dy
        if dy == 0:
            return charge >= abs(dx)
        if dy == 1:
            return charge >= abs(dx) + 1
        return False
    else:
        if dy < 0:
            dx, dy = -dx, -dy
        if dx < 0:
            dx = -dx
        if dx == 0:
            return charge >= abs(dy)
        if dx == 1:
            return charge >= abs(dy) + 1
        return False

def main():
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    charge = int(input())
    print("Y" if can_reach_destination(start, end, charge) else "N")

if __name__ == "__main__":
    main()

