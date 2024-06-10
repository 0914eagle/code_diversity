
import numpy as np

def point(a):
    return np.array(a)

def cross_product(a, b):
    return np.cross(a, b)

def dot_product(a, b):
    return np.dot(a, b)

def angle_between_planes(a, b, c, d):
    ab = point(b) - point(a)
    bc = point(c) - point(b)
    cd = point(d) - point(c)
    x = cross_product(ab, bc)
    y = cross_product(bc, cd)
    return np.rad2deg(np.arccos(dot_product(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))))

def main():
    a = [0, 0, 0]
    b = [3, 0, 0]
    c = [3, 4, 0]
    d = [0, 4, 0]
    print(angle_between_planes(a, b, c, d))

if __name__ == '__main__':
    main()

