
def is_regular_polygon_possible(angle):
    return angle % 180 == 0 or angle % 90 == 0

def main():
    tests = int(input())
    for _ in range(tests):
        angle = int(input())
        if is_regular_polygon_possible(angle):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

