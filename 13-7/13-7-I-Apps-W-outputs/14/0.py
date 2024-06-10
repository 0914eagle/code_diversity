
def get_min_cost(c_matrix, a_matrix):
    # Initialize the minimum cost to turn all digits into 1
    min_cost = 0
    
    # Loop through each row of the wall
    for i in range(len(a_matrix)):
        # Loop through each column of the wall
        for j in range(len(a_matrix[0])):
            # If the current square contains a digit
            if a_matrix[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = c_matrix[a_matrix[i][j]][1]
                # Add the cost to the minimum cost
                min_cost += cost
    
    return min_cost

def main():
    # Read the input data
    h, w = map(int, input().split())
    c_matrix = []
    for i in range(10):
        row = list(map(int, input().split()))
        c_matrix.append(row)
    a_matrix = []
    for i in range(h):
        row = list(map(int, input().split()))
        a_matrix.append(row)
    
    # Calculate the minimum cost to turn all digits into 1
    min_cost = get_min_cost(c_matrix, a_matrix)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

