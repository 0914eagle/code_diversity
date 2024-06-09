
import math

def get_energy_contribution(x, y, e):
    return e

def get_line_length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_shortest_continuous_line(lamps):
    # Sort lamps by their x-coordinate
    lamps.sort(key=lambda x: x[0])
    
    # Initialize the shortest line length to infinity
    shortest_line_length = float('inf')
    
    # Iterate over all possible lines
    for i in range(len(lamps)):
        for j in range(i+1, len(lamps)):
            # Get the coordinates of the two lamps
            x1, y1 = lamps[i][0], lamps[i][1]
            x2, y2 = lamps[j][0], lamps[j][1]
            
            # Get the energy contribution of the two lamps
            e1 = get_energy_contribution(x1, y1, lamps[i][2])
            e2 = get_energy_contribution(x2, y2, lamps[j][2])
            
            # Get the length of the line segment
            line_length = get_line_length(x1, y1, x2, y2)
            
            # Check if the line segment is the shortest continuous line
            if e1 + e2 == 0 and line_length < shortest_line_length:
                shortest_line_length = line_length
    
    return shortest_line_length

def main():
    # Read the number of lamps
    n = int(input())
    
    # Read the coordinates and energy contribution of each lamp
    lamps = []
    for i in range(n):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    
    # Get the shortest continuous line
    shortest_line_length = get_shortest_continuous_line(lamps)
    
    # Print the output
    if shortest_line_length == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(shortest_line_length)

if __name__ == '__main__':
    main()

