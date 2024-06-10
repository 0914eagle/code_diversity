
import math

def get_center(p1, p2, p3, p4):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4
    
    denom = 2 * (x1 * (y2 - z3) + y1 * (z3 - x2) + z1 * (x2 - y3))
    x_c = (x1 * x1 + y1 * y1 + z1 * z1) * (y2 - z3) + (x2 * x2 + y2 * y2 + z2 * z2) * (z3 - x1) + (x3 * x3 + y3 * y3 + z3 * z3) * (x1 - y2)
    x_c /= denom
    
    y_c = (x1 * x1 + y1 * y1 + z1 * z1) * (z2 - y3) + (x2 * x2 + y2 * y2 + z2 * z2) * (x3 - z1) + (x3 * x3 + y3 * y3 + z3 * z3) * (y1 - x2)
    y_c /= denom
    
    z_c = (x1 * x1 + y1 * y1 + z1 * z1) * (x2 - z3) + (x2 * x2 + y2 * y2 + z2 * z2) * (y3 - x1) + (x3 * x3 + y3 * y3 + z3 * z3) * (z1 - y2)
    z_c /= denom
    
    return x_c, y_c, z_c

def get_input():
    p1 = tuple(map(float, input().split()))
    p2 = tuple(map(float, input().split()))
    p3 = tuple(map(float, input().split()))
    p4 = tuple(map(float, input().split()))
    return p1, p2, p3, p4

def main():
    p1, p2, p3, p4 = get_input()
    x_c, y_c, z_c = get_center(p1, p2, p3, p4)
    print(f"{x_c:.4f} {y_c:.4f} {z_c:.4f}")

if __name__ == '__main__':
    main()

