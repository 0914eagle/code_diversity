
def is_regular_polygon_possible(angle):
    return angle in [0, 30, 45, 60, 90]

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        angle = int(input())
        if is_regular_polygon_possible(angle):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

