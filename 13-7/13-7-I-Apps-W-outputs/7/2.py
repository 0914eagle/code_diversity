
def is_polygon_possible(angle):
    return angle % 180 == 0 or angle % 90 == 0

def solve():
    num_tests = int(input())
    for _ in range(num_tests):
        angle = int(input())
        if is_polygon_possible(angle):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()

