
def find_points(n, m, k):
    # Iterate through all possible values of x1
    for x1 in range(n + 1):
        # Calculate the value of x2 and y2 based on the area formula
        x2 = (k * x1 - n * m) / (k - 1)
        y2 = (k * x1 - n * m) / (k - 1)
        # Check if x2 and y2 are integers and within the required range
        if x2.is_integer() and 0 <= x2 <= n and 0 <= y2 <= m:
            # Calculate the value of x3 and y3 based on the area formula
            x3 = k - x1 - y2
            y3 = k - x1 - y2
            # Check if x3 and y3 are integers and within the required range
            if x3.is_integer() and 0 <= x3 <= n and 0 <= y3 <= m:
                return [int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)]
    return "NO"

def main():
    n, m, k = map(int, input().split())
    points = find_points(n, m, k)
    if points == "NO":
        print("NO")
    else:
        print("YES")
        for i in range(3):
            print(points[i], points[i + 3])

if __name__ == '__main__':
    main()

