
def can_see_belle(belle_x, belle_y, rect_x1, rect_y1, rect_x2, rect_y2):
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def is_tree_blocking(x, y, rect_x1, rect_y1, rect_x2, rect_y2):
        return rect_x1 <= x <= rect_x2 and rect_y1 <= y <= rect_y2

    closest_tree = None
    min_distance = float('inf')

    for x in range(rect_x1, rect_x2 + 1):
        for y in range(rect_y1, rect_y2 + 1):
            if is_tree_blocking(x, y, rect_x1, rect_y1, rect_x2, rect_y2):
                if distance(0, 0, x, y) < min_distance:
                    min_distance = distance(0, 0, x, y)
                    closest_tree = (x, y)

    if closest_tree is None:
        return "Yes"
    else:
        return f"No\n{closest_tree[0]} {closest_tree[1]}"

if __name__ == "__main__":
    belle_x, belle_y = map(int, input().split())
    rect_x1, rect_y1, rect_x2, rect_y2 = map(int, input().split())
    
    print(can_see_belle(belle_x, belle_y, rect_x1, rect_y1, rect_x2, rect_y2))
