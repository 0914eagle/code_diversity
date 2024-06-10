
def get_wall_height(h, w, n, x):
    # Calculate the total height of the wall
    total_height = 0
    for i in range(n):
        total_height += x[i]
    # Check if the total height is greater than or equal to the height of the wall
    if total_height >= h:
        return True
    else:
        return False

def get_wall_width(w, n, x):
    # Calculate the total width of the wall
    total_width = 0
    for i in range(n):
        total_width += x[i]
    # Check if the total width is greater than or equal to the width of the wall
    if total_width >= w:
        return True
    else:
        return False

def main():
    h, w, n = map(int, input().split())
    x = list(map(int, input().split()))
    if get_wall_height(h, w, n, x) and get_wall_width(w, n, x):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

