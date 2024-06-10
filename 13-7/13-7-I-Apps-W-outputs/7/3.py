
def is_regular_polygon_possible(angle):
    # Check if the angle is valid
    if angle < 0 or angle > 180:
        return False
    
    # Check if the angle is a multiple of 30 degrees
    if angle % 30 != 0:
        return False
    
    # Check if the angle is a multiple of 60 degrees
    if angle % 60 != 0:
        return False
    
    # Check if the angle is a multiple of 90 degrees
    if angle % 90 != 0:
        return False
    
    # If all the above conditions are met, then the angle is valid
    return True

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

