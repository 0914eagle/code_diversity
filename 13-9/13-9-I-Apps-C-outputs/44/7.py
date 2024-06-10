
def get_splitters(a, b, c, d, n):
    # Initialize the splitters dictionary
    splitters = {}
    
    # Initialize the input and output belts
    input_belt = 0
    output_belts = [1, 2]
    
    # Iterate through the desired ratios
    for i in range(n):
        # Calculate the ratio of the input to the first output
        ratio = a / (a + b)
        
        # Add the splitter to the dictionary
        splitters[i] = (input_belt, output_belts[0], ratio)
        
        # Update the input and output belts
        input_belt = output_belts[0]
        output_belts[0] = output_belts[1]
        output_belts[1] = i + 3
    
    # Return the splitters dictionary
    return splitters

def get_network(a, b, c, d):
    # Calculate the number of splitters needed
    n = (c * d) // (a * b)
    
    # Get the splitters
    splitters = get_splitters(a, b, c, d, n)
    
    # Return the splitters dictionary
    return splitters

def main():
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # Get the network
    splitters = get_network(a, b, c, d)
    
    # Print the number of splitters
    print(len(splitters))
    
    # Print the splitters
    for i, (input_belt, output_belt, ratio) in splitters.items():
        print(input_belt, output_belt)
    
if __name__ == '__main__':
    main()

