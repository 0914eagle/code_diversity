
def get_cost(i, j, c):
    return c[i, j]

def get_min_cost(A, c):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through each row and column of the wall
    for i in range(len(A)):
        for j in range(len(A[0])):
            # If the current square contains a digit
            if A[i, j] != -1:
                # Get the cost of turning the current digit into 1
                cost = get_cost(A[i, j], 1, c)
                
                # If the cost is less than the minimum cost, update the minimum cost
                if cost < min_cost:
                    min_cost = cost
    
    return min_cost

def main():
    # Read the input from stdin
    H, W = map(int, input().split())
    c = []
    for i in range(10):
        c.append(list(map(int, input().split())))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    
    # Get the minimum cost to turn every digit on the wall into 1
    min_cost = get_min_cost(A, c)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

