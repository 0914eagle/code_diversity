
import math

def get_candle_coordinates(n):
    candle_coordinates = []
    for i in range(n):
        x, y = map(float, input().split())
        candle_coordinates.append((x, y))
    return candle_coordinates

def get_cut_coefficients(m):
    cut_coefficients = []
    for i in range(m):
        a, b, c = map(float, input().split())
        cut_coefficients.append((a, b, c))
    return cut_coefficients

def is_cut_valid(cut_coefficients, candle_coordinates):
    for cut in cut_coefficients:
        a, b, c = cut
        for candle in candle_coordinates:
            x, y = candle
            if a*x + b*y + c == 0:
                return False
    return True

def main():
    n, m, r = map(int, input().split())
    candle_coordinates = get_candle_coordinates(n)
    cut_coefficients = get_cut_coefficients(m)
    if is_cut_valid(cut_coefficients, candle_coordinates):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

