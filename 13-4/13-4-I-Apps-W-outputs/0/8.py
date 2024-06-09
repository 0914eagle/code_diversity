
def solve(s):
    colors = ["A", "B", "C"]
    cells = [c for c in s if c not in "."]
    for color in colors:
        if color not in cells:
            return "No"
    return "Yes"

