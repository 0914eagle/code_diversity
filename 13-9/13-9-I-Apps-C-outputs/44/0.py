
def get_splitters(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the list of splitters
    splitters = []
    # Initialize the input and output belts
    input_belt = 0
    output_belts = [1, 2]
    # While there are still boxes to distribute
    while any(boxes_left := sum(output_belts)):
        # Find the ratio of boxes that need to be distributed to each output belt
        output_ratios = [c/(c+d), d/(c+d)]
        # Find the number of boxes that can be sent to each output belt
        output_boxes = [int(boxes_left * ratio) for ratio in output_ratios]
        # Create a new splitter with the given ratio
        splitters.append([a, b])
        # Connect the input belt to the new splitter
        input_belt = n
        # Connect the new splitter to the output belts
        output_belts = [input_belt, input_belt]
        # Increment the number of splitters
        n += 1
    # Return the number of splitters and the list of splitters
    return n, splitters

def main():
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # Get the number of splitters and the list of splitters
    n, splitters = get_splitters(a, b, c, d)
    # Print the number of splitters
    print(n)
    # Print the list of splitters
    for i, splitter in enumerate(splitters):
        print(f"{splitter[0]} {splitter[1]}")

if __name__ == '__main__':
    main()

