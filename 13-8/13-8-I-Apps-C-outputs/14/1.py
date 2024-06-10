
import math

def get_center(p1, p2, p3, p4):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4
    
    # Calculate the equations of the planes that pass through the points
    a1 = (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1)
    b1 = (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1)
    c1 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    d1 = - (a1 * x1 + b1 * y1 + c1 * z1)
    
    a2 = (y3 - y2) * (z4 - z2) - (z3 - z2) * (y4 - y2)
    b2 = (z3 - z2) * (x4 - x2) - (x3 - x2) * (z4 - z2)
    c2 = (x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2)
    d2 = - (a2 * x2 + b2 * y2 + c2 * z2)
    
    # Calculate the intersection of the two planes
    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1)
    z = (a1 * b2 * d2 - a2 * b1 * d1) / (a1 * b2 - a2 * b1)
    
    return x, y, z

def main():
    p1 = [0, 0, 0]
    p2 = [1, 0, 0]
    p3 = [0, 1, 0]
    p4 = [0, 0, 1]
    
    center = get_center(p1, p2, p3, p4)
    print(center)

if __name__ == '__main__':
    main()

