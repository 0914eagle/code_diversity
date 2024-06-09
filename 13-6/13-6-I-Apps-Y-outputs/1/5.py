
import math

def get_diagonals(vertices):
    
    diagonals = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if j == len(vertices)-1:
                diagonals.append((vertices[i], vertices[j], vertices[0]))
            else:
                diagonals.append((vertices[i], vertices[j], vertices[j+1]))
    return diagonals

def get_intersections(diagonals):
    
    count = 0
    for i in range(len(diagonals)):
        for j in range(i+1, len(diagonals)):
            d1 = diagonals[i]
            d2 = diagonals[j]
            if do_intersect(d1, d2):
                count += 1
    return count

def do_intersect(d1, d2):
    
    x1, y1 = d1[0]
    x2, y2 = d1[1]
    x3, y3 = d1[2]
    x4, y4 = d2[0]
    x5, y5 = d2[1]
    x6, y6 = d2[2]
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if denom == 0:
        return False
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
    return 0 <= t <= 1 and 0 <= u <= 1

def main():
    vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    diagonals = get_diagonals(vertices)
    print(get_intersections(diagonals))

if __name__ == '__main__':
    main()

