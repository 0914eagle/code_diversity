
def read_input():
    n = int(input())
    hamsters = input()
    return n, hamsters

def optimize_hamsters(n, hamsters):
    # Initialize the number of minutes required to be 0
    minutes = 0
    
    # Loop through each pair of hamsters
    for i in range(0, n, 2):
        # If the hamsters in the pair are not standing, stand them up
        if hamsters[i] == 'x' and hamsters[i+1] == 'x':
            hamsters = hamsters[:i] + 'X' + hamsters[i+1:]
            minutes += 1
    
    # Return the number of minutes required and the optimized hamsters' position
    return minutes, hamsters

def main():
    # Read the input
    n, hamsters = read_input()
    
    # Optimize the hamsters' position
    minutes, optimized_hamsters = optimize_hamsters(n, hamsters)
    
    # Print the output
    print(minutes)
    print(optimized_hamsters)

if __name__ == '__main__':
    main()

