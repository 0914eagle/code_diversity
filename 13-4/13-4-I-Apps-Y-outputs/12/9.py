
import math

def get_volume(length, width, height):
    return length * width * height

def get_perimeter(length, width, height):
    return 2 * (length + width + height)

def solve(L):
    # Initialize variables
    length = 0
    width = 0
    height = 0
    max_volume = 0
    
    # Loop through all possible combinations of length, width, and height
    for i in range(1, int(L / 3) + 1):
        for j in range(1, int(L / 2) + 1):
            for k in range(1, int(L / 6) + 1):
                # Calculate the volume and perimeter of the current cuboid
                volume = get_volume(i, j, k)
                perimeter = get_perimeter(i, j, k)
                
                # Check if the current cuboid has the maximum volume and is a feasible solution
                if volume > max_volume and perimeter == L:
                    max_volume = volume
                    length = i
                    width = j
                    height = k
    
    # Return the maximum volume and the dimensions of the cuboid
    return max_volume, length, width, height

if __name__ == '__main__':
    L = float(input())
    max_volume, length, width, height = solve(L)
    print(f"{max_volume:.10f}")

