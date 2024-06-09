
def is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    if x2 <= x3 or x1 >= x4 or y2 <= y3 or y1 >= y4:
        return "YES"
    if x2 <= x5 or x1 >= x6 or y2 <= y5 or y1 >= y6:
        return "YES"
    return "NO"

# Input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output
print(is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))
