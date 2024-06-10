
def get_shortest_line(lamp_positions):
    # Calculate the total energy of all lamps
    total_energy = sum(lamp_position[2] for lamp_position in lamp_positions)
    
    # Initialize the shortest line length to infinity
    shortest_line_length = float('inf')
    
    # Iterate through all possible line segments
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            # Calculate the line segment length
            line_segment_length = ((lamp_positions[i][0] - lamp_positions[j][0]) ** 2 + (lamp_positions[i][1] - lamp_positions[j][1]) ** 2) ** 0.5
            
            # Calculate the energy contribution of the line segment
            line_segment_energy = sum(lamp_position[2] for lamp_position in lamp_positions[i:j+1])
            
            # If the energy contribution of the line segment is equal to the total energy, we have found the shortest line
            if line_segment_energy == total_energy:
                # Return the length of the line segment
                return line_segment_length
            
            # If the line segment energy is less than the total energy, we need to continue searching
            if line_segment_energy < total_energy:
                # Update the shortest line length if the line segment length is shorter than the current shortest line length
                shortest_line_length = min(shortest_line_length, line_segment_length)
    
    # If no line segment with equal energy contribution was found, return the shortest line length
    return shortest_line_length

def main():
    # Read the number of lamps from stdin
    num_lamps = int(input())
    
    # Read the lamp positions and energies from stdin
    lamp_positions = []
    for _ in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y, energy))
    
    # Call the get_shortest_line function to find the shortest line length
    shortest_line_length = get_shortest_line(lamp_positions)
    
    # Print the result
    print(shortest_line_length)

if __name__ == '__main__':
    main()

