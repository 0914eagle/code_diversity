
import math

def get_candle_locations(n, r):
    candle_locations = []
    for i in range(n):
        x, y = map(float, input().split())
        if math.sqrt(x**2 + y**2) < r:
            candle_locations.append((x, y))
    return candle_locations

def get_cut_lines(m):
    cut_lines = []
    for i in range(m):
        a, b, c = map(float, input().split())
        if a != 0 and b != 0:
            cut_lines.append((a, b, c))
    return cut_lines

def is_candle_on_cut_line(candle_location, cut_line):
    a, b, c = cut_line
    x, y = candle_location
    return a*x + b*y + c == 0

def is_cut_line_valid(cut_line, candle_locations):
    for candle_location in candle_locations:
        if is_candle_on_cut_line(candle_location, cut_line):
            return True
    return False

def is_cut_valid(cut_lines, candle_locations):
    for cut_line in cut_lines:
        if not is_cut_line_valid(cut_line, candle_locations):
            return False
    return True

def solve(n, m, r):
    candle_locations = get_candle_locations(n, r)
    cut_lines = get_cut_lines(m)
    if is_cut_valid(cut_lines, candle_locations):
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    print(solve(n, m, r))

