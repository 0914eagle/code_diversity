
def is_polygon_possible(angle):
    # Check if the angle is valid
    if angle < 0 or angle > 180:
        return False
    
    # Check if the angle is a multiple of 180 degrees
    if angle % 180 == 0:
        return False
    
    # Check if the angle is a multiple of 90 degrees
    if angle % 90 == 0:
        return True
    
    # Check if the angle is a multiple of 45 degrees
    if angle % 45 == 0:
        return True
    
    # Otherwise, it is not possible to build a regular polygon with the given angle
    return False

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

