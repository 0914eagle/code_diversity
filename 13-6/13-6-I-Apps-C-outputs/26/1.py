
def read_input():
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x_coords = list(map(float, input().split()))
    min_sand = []
    for i in range(n):
        min_sand.append(list(map(float, input().split())))
    max_sand = []
    for i in range(n):
        max_sand.append(list(map(float, input().split())))
    return n, m, w, h, volumes, x_coords, min_sand, max_sand

def f1(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    # Initialize the variables
    section_heights = [0] * n
    total_volume = sum(volumes)
    current_volume = 0
    current_color = 0
    current_x = 0
    
    # Loop through each section
    for i in range(n):
        # Calculate the volume of sand for each section
        volume = 0
        for j in range(m):
            volume += (max_sand[i][j] - min_sand[i][j]) * volumes[j]
        
        # Add the volume to the current section
        section_heights[i] += volume
        current_volume += volume
        
        # Update the current color and x coordinate
        current_color = (current_color + 1) % m
        current_x = x_coords[i]
    
    # Calculate the maximum height and minimum height
    max_height = max(section_heights)
    min_height = min(section_heights)
    
    # Calculate the difference between the maximum and minimum heights
    difference = max_height - min_height
    
    # Return the difference rounded to 3 decimal places
    return round(difference, 3)

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n, m, w, h, volumes, x_coords, min_sand, max_sand = read_input()
    print(f1(n, m, w, h, volumes, x_coords, min_sand, max_sand))

