
def get_square_killer_size(memory):
    # Initialize variables
    max_size = 0
    size = 0
    current_row = 0
    current_col = 0
    direction = 0
    visited = [[False for _ in range(len(memory[0]))] for _ in range(len(memory))]
    
    # Iterate through the memory matrix
    for row in range(len(memory)):
        for col in range(len(memory[0])):
            # If the current position is not visited and is a 1, start a new square killer
            if not visited[row][col] and memory[row][col] == "1":
                size = 1
                current_row = row
                current_col = col
                direction = 0
                visited[row][col] = True
                
                # Iterate through the square killer
                while size > 0:
                    # If the current position is not visited and is a 1, increment the size and mark it as visited
                    if not visited[current_row][current_col] and memory[current_row][current_col] == "1":
                        size += 1
                        visited[current_row][current_col] = True
                    
                    # Move to the next position in the direction of the current square killer
                    if direction == 0:
                        current_row += 1
                    elif direction == 1:
                        current_col += 1
                    elif direction == 2:
                        current_row -= 1
                    else:
                        current_col -= 1
                    
                    # If the current position is out of bounds, break the loop
                    if current_row < 0 or current_row >= len(memory) or current_col < 0 or current_col >= len(memory[0]):
                        break
                    
                # If the size of the current square killer is greater than the maximum size, update the maximum size
                if size > max_size:
                    max_size = size
    
    # Return the maximum size
    return max_size

def main():
    # Read the input
    R, C = map(int, input().split())
    memory = []
    for _ in range(R):
        memory.append(input())
    
    # Call the function to get the size of the largest square killer
    largest_square_killer_size = get_square_killer_size(memory)
    
    # Print the output
    print(largest_square_killer_size)

if __name__ == '__main__':
    main()

