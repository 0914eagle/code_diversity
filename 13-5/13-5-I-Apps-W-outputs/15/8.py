
def get_regular_polygon(angle):
    # Iterate through possible numbers of vertices
    for n in range(3, 998244354):
        # Check if n is a valid number of vertices for a regular polygon
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            continue
        # Calculate the interior angle of each vertex
        interior_angle = (n - 2) * 180 / n
        # Check if the interior angle is equal to the given angle
        if interior_angle == angle:
            return n
    # If no polygon is found, return -1
    return -1

def main():
    T = int(input())
    for _ in range(T):
        angle = int(input())
        print(get_regular_polygon(angle))

if __name__ == '__main__':
    main()

