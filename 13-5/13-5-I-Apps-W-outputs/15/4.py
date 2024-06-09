
def find_regular_polygon(angle):
    n = 3
    while n <= 998244353:
        if n_gon_angle(n) == angle:
            return n
        n += 1
    return -1

def n_gon_angle(n):
    return 360 / n

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        angle = int(input())
        print(find_regular_polygon(angle))

