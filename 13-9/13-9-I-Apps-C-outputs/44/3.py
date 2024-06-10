
def get_splitter_config(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the configuration of the splitters as a list of pairs (l, r), where l is the index of the splitter connected to the left output and r is the index of the splitter connected to the right output
    config = []
    # While there are still boxes to be distributed
    while c > 0 or d > 0:
        # If the number of boxes to be distributed is greater than the total number of boxes that can be sent through all the splitters
        if c + d > a + b:
            # Calculate the ratio of boxes to be sent to each output based on the current configuration
            l_ratio = a / (a + b)
            r_ratio = b / (a + b)
            # If the left output has more boxes to be sent than the right output
            if l_ratio > r_ratio:
                # Send the difference between the left and right output to the right output
                config.append((-1, n))
                d -= l_ratio - r_ratio
            # If the right output has more boxes to be sent than the left output
            else:
                # Send the difference between the left and right output to the left output
                config.append((n, -1))
                c -= r_ratio - l_ratio
        # If the number of boxes to be distributed is less than the total number of boxes that can be sent through all the splitters
        else:
            # Calculate the ratio of boxes to be sent to each output based on the current configuration
            l_ratio = c / (c + d)
            r_ratio = d / (c + d)
            # If the left output has more boxes to be sent than the right output
            if l_ratio > r_ratio:
                # Send the difference between the left and right output to the right output
                config.append((-1, -2))
                d = 0
            # If the right output has more boxes to be sent than the left output
            else:
                # Send the difference between the left and right output to the left output
                config.append((-2, -1))
                c = 0
        # Increment the number of splitters
        n += 1
    # Return the number of splitters and the configuration of the splitters
    return n, config

def main():
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # Get the configuration of the splitters
    n, config = get_splitter_config(a, b, c, d)
    # Print the number of splitters
    print(n)
    # Print the configuration of the splitters
    for l, r in config:
        print(l, r)

if __name__ == '__main__':
    main()

