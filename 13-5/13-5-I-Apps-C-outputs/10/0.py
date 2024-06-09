
import math

def get_candle_locations(n):
    candle_locations = []
    for i in range(n):
        x, y = map(float, input().split())
        candle_locations.append((x, y))
    return candle_locations

def get_cut_lines(m):
    cut_lines = []
    for i in range(m):
        a, b, c = map(float, input().split())
        cut_lines.append((a, b, c))
    return cut_lines

def is_valid_cut(cut, candle_locations):
    for candle in candle_locations:
        if cut[0] * candle[0] + cut[1] * candle[1] + cut[2] == 0:
            return False
    return True

def is_valid_candle(candle, cut_lines):
    for cut in cut_lines:
        if cut[0] * candle[0] + cut[1] * candle[1] + cut[2] == 0:
            return False
    return True

def is_valid_partition(candle_locations, cut_lines):
    for candle in candle_locations:
        if not is_valid_candle(candle, cut_lines):
            return False
    for cut in cut_lines:
        if not is_valid_cut(cut, candle_locations):
            return False
    return True

def main():
    n, m, r = map(int, input().split())
    candle_locations = get_candle_locations(n)
    cut_lines = get_cut_lines(m)
    if is_valid_partition(candle_locations, cut_lines):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

