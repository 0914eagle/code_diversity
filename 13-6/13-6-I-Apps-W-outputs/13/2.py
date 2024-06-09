
def get_largest_rectangle(matrix):
    # Initialize variables
    max_area = 0
    current_area = 0
    stack = []
    
    # Iterate through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # If the current cell is 1, push its index to the stack and update the current area
            if matrix[i][j] == "1":
                stack.append(j)
                current_area += 1
            # If the current cell is 0, pop indices from the stack and update the current area
            elif matrix[i][j] == "0":
                while stack and stack[-1] > j:
                    stack.pop()
                    current_area -= 1
                if stack and stack[-1] == j:
                    stack.pop()
                    current_area -= 1
            # Update the max area if the current area is greater than the max area
            if current_area > max_area:
                max_area = current_area
    
    # Return the max area
    return max_area

def main():
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(get_largest_rectangle(matrix))

if __name__ == '__main__':
    main()

