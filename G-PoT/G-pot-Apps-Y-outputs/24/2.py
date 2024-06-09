
# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Check if some part of the white sheet can be seen
if x2 <= x3 or x1 >= x4 or y2 <= y3 or y1 >= y4 or x2 <= x5 or x1 >= x6 or y2 <= y5 or y1 >= y6:
    print("YES")
else:
    print("NO")
