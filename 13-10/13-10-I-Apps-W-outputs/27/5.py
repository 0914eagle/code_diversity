
def boring_pairs(planets, paths):
    # Initialize a set to store the boring pairs
    boring_pairs = set()
    
    # Iterate over each path
    for path in paths:
        # Get the two planets connected by the path
        planet1, planet2 = path[0], path[1]
        
        # Check if the XOR of the path curiosity is equal to 0
        if xor(path[2]) == 0:
            # Add the boring pair to the set
            boring_pairs.add((planet1, planet2))
    
    return boring_pairs

def xor(num):
    # Initialize a variable to store the result
    result = 0
    
    # Iterate over each digit of the number
    for digit in str(num):
        # Add the digit to the result
        result += int(digit)
    
    return result

def main():
    # Read the number of planets and paths
    num_planets, num_paths = map(int, input().split())
    
    # Initialize a list to store the paths
    paths = []
    
    # Read the paths
    for _ in range(num_paths):
        path = list(map(int, input().split()))
        paths.append(path)
    
    # Get the boring pairs
    boring_pairs = boring_pairs(num_planets, paths)
    
    # Print the number of boring pairs after each path is destroyed
    for i in range(num_paths):
        print(len(boring_pairs))
        # Destroy the path
        paths.pop(i)
        # Update the boring pairs
        boring_pairs = boring_pairs(num_planets, paths)

if __name__ == '__main__':
    main()

