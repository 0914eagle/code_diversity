
def get_max_time(a, M):
    # Calculate the total time when the lamp is lit
    total_time = 0
    for i in range(len(a) - 1):
        total_time += a[i + 1] - a[i]
    
    # If the lamp is already lit at the end of the program, add the time until M
    if a[-1] < M:
        total_time += M - a[-1]
    
    return total_time

def insert_element(a, x, M):
    # Insert the element into the program
    a.insert(0, x)
    
    # Sort the program in ascending order
    a.sort()
    
    # Remove any elements that are greater than M
    a = [i for i in a if i <= M]
    
    return a

def get_optimal_program(a, M):
    # Initialize the optimal program and total time
    optimal_program = a
    optimal_time = get_max_time(a, M)
    
    # Iterate over all possible insertion points
    for i in range(len(a)):
        # Insert the element into the program
        new_program = insert_element(a[:i] + a[i:], a[i - 1], M)
        
        # Calculate the total time for the new program
        new_time = get_max_time(new_program, M)
        
        # If the total time is greater than the optimal time, update the optimal program and time
        if new_time > optimal_time:
            optimal_program = new_program
            optimal_time = new_time
    
    return optimal_program

def main():
    # Read the input
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Get the optimal program
    optimal_program = get_optimal_program(a, M)
    
    # Print the optimal time
    print(get_max_time(optimal_program, M))

if __name__ == '__main__':
    main()

