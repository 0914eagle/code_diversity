
import math

def is_polygon_possible(angle):
    
    if angle == 0 or angle == 180:
        return False
    return True

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        angle = int(input())
        if is_polygon_possible(angle):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

