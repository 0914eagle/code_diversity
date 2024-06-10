
import math

def is_regular_polygon_possible(angle):
    # Check if the angle is valid
    if angle < 0 or angle > 180:
        return False
    
    # Check if the angle is a multiple of 30 degrees
    if angle % 30 != 0:
        return False
    
    # Check if the angle is a right angle
    if angle == 90:
        return False
    
    # Check if the angle is a multiple of 30 degrees and a right angle
    if angle % 30 == 0 and angle != 90:
        return True
    
    return False

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

