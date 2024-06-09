
import math

def get_input():
    n, m, r = map(int, input().split())
    candles = []
    for i in range(n):
        x, y = map(int, input().split())
        candles.append((x, y))
    lines = []
    for i in range(m):
        a, b, c = map(int, input().split())
        lines.append((a, b, c))
    return n, m, r, candles, lines

def is_valid_candle(candle, r):
    return math.sqrt(candle[0]**2 + candle[1]**2) < r

def is_valid_line(line, candles, r):
    a, b, c = line
    for candle in candles:
        x, y = candle
        if a*x + b*y + c == 0 and math.sqrt(x**2 + y**2) < r:
            return False
    return True

def is_valid_cuts(n, m, r, candles, lines):
    for line in lines:
        if not is_valid_line(line, candles, r):
            return False
    for candle in candles:
        if not is_valid_candle(candle, r):
            return False
    return True

def f1():
    n, m, r, candles, lines = get_input()
    return "yes" if is_valid_cuts(n, m, r, candles, lines) else "no"

if __name__ == '__main__':
    print(f1())

