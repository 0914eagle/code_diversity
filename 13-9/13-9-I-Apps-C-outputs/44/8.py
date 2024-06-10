
def get_splitter_configuration(a, b, c, d):
    # Initialize the splitter configuration
    splitters = []
    output_belts = [0, 0]
    
    # While there are still boxes to be distributed
    while sum(output_belts) < c + d:
        # Find the next splitter to use
        next_splitter = get_next_splitter(a, b, c, d, splitters)
        
        # Add the splitter to the configuration
        splitters.append(next_splitter)
        
        # Update the output belts
        output_belts[next_splitter[0]] += a / (a + b)
        output_belts[next_splitter[1]] += b / (a + b)
    
    # Return the configuration
    return splitters

def get_next_splitter(a, b, c, d, splitters):
    # Find the splitter with the smallest number of boxes received
    smallest_received = float('inf')
    next_splitter = None
    for i in range(len(splitters)):
        received = sum(splitters[i])
        if received < smallest_received:
            smallest_received = received
            next_splitter = i
    
    # Return the next splitter
    return next_splitter

def main():
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # Get the splitter configuration
    splitters = get_splitter_configuration(a, b, c, d)
    
    # Print the number of splitters used
    print(len(splitters))
    
    # Print the splitter configuration
    for i in range(len(splitters)):
        print(splitters[i][0], splitters[i][1])

if __name__ == '__main__':
    main()

