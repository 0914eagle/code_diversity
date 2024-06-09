
def get_input():
    return map(float, input().split())

def cross_product(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def get_angle(v1, v2):
    x = cross_product(v1, v2)
    y = cross_product(v2, v1)
    return math.degrees(math.acos(dot_product(x, y)/(math.sqrt(dot_product(x, x))*math.sqrt(dot_product(y, y)))))

def main():
    a = get_input()
    b = get_input()
    c = get_input()
    d = get_input()
    ab = [b[0]-a[0], b[1]-a[1], b[2]-a[2]]
    bc = [c[0]-b[0], c[1]-b[1], c[2]-b[2]]
    cd = [d[0]-c[0], d[1]-c[1], d[2]-c[2]]
    print(get_angle(ab, bc))
    print(get_angle(bc, cd))

if __name__ == '__main__':
    main()

