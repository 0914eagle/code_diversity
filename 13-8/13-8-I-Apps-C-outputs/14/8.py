
import math

def get_centre(p1, p2, p3, p4):
    v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
    v3 = [p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2]]
    
    cross1 = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
    cross2 = [v2[1] * v3[2] - v2[2] * v3[1], v2[2] * v3[0] - v2[0] * v3[2], v2[0] * v3[1] - v2[1] * v3[0]]
    cross3 = [v3[1] * v1[2] - v3[2] * v1[1], v3[2] * v1[0] - v3[0] * v1[2], v3[0] * v1[1] - v3[1] * v1[0]]
    
    dot = cross1[0] * cross2[0] + cross1[1] * cross2[1] + cross1[2] * cross2[2]
    det = cross1[0] * cross3[0] + cross1[1] * cross3[1] + cross1[2] * cross3[2]
    
    x = (dot * (p1[1] * p2[2] - p1[2] * p2[1]) + det * (p1[2] * p3[1] - p1[1] * p3[2])) / (2 * (v1[1] * v2[2] - v1[2] * v2[1]))
    y = (dot * (p1[2] * p2[0] - p1[0] * p2[2]) + det * (p1[0] * p3[2] - p1[2] * p3[0])) / (2 * (v1[2] * v2[0] - v1[0] * v2[2]))
    z = (dot * (p1[0] * p2[1] - p1[1] * p2[0]) + det * (p1[1] * p3[0] - p1[0] * p3[1])) / (2 * (v1[0] * v2[1] - v1[1] * v2[0]))
    
    return [x, y, z]

def main():
    p1 = [float(x) for x in input().split()]
    p2 = [float(x) for x in input().split()]
    p3 = [float(x) for x in input().split()]
    p4 = [float(x) for x in input().split()]
    
    centre = get_centre(p1, p2, p3, p4)
    print(" ".join(map(str, centre)))

if __name__ == '__main__':
    main()

