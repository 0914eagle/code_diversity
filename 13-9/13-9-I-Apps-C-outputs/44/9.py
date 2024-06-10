
def find_splitters(a, b, c, d):
    # Initialize the number of splitters to be used
    n = 0
    
    # Initialize the list of splitters
    splitters = []
    
    # Initialize the input and output belts
    input_belts = [0]
    output_belts = [0, 0]
    
    # While there are more output belts to be connected
    while len(output_belts) < 2:
        # Find the next splitter to be added
        next_splitter = find_next_splitter(input_belts, output_belts, a, b, c, d)
        
        # If no splitter can be added, return None
        if next_splitter is None:
            return None
        
        # Add the next splitter to the list of splitters
        splitters.append(next_splitter)
        
        # Update the input and output belts
        input_belts.append(next_splitter[0])
        output_belts.append(next_splitter[1])
        
        # Increment the number of splitters used
        n += 1
    
    # Return the list of splitters
    return splitters

def find_next_splitter(input_belts, output_belts, a, b, c, d):
    # Initialize the best splitter to be None
    best_splitter = None
    
    # Initialize the best efficiency to be 0
    best_efficiency = 0
    
    # Iterate over the possible splitters
    for i in range(len(input_belts)):
        for j in range(len(output_belts)):
            # If the splitter has already been used, skip it
            if i == j:
                continue
            
            # Calculate the efficiency of the splitter
            efficiency = calculate_efficiency(input_belts[i], output_belts[j], a, b, c, d)
            
            # If the efficiency is greater than the best efficiency, set it as the best splitter
            if efficiency > best_efficiency:
                best_splitter = (i, j)
                best_efficiency = efficiency
    
    # Return the best splitter
    return best_splitter

def calculate_efficiency(input_belts, output_belts, a, b, c, d):
    # Calculate the efficiency of the splitter
    efficiency = (a * c + b * d) / (a * c + b * d + a * (1 - c) + b * (1 - d))
    
    # Return the efficiency
    return efficiency

if __name__ == '__main__':
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # Find the splitters
    splitters = find_splitters(a, b, c, d)
    
    # If no splitters can be found, print None
    if splitters is None:
        print("None")
    else:
        # Print the number of splitters
        print(len(splitters))
        
        # Print the splitters
        for splitter in splitters:
            print(splitter[0], splitter[1])

