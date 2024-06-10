
def get_min_people(log):
    # Initialize a set to store the unique visitors
    visitors = set()
    # Iterate through the log
    for event in log:
        # If the event is "+", add the current visitor to the set
        if event == "+":
            visitors.add(len(visitors))
        # If the event is "-", remove the current visitor from the set
        elif event == "-":
            visitors.remove(len(visitors) - 1)
    # Return the minimum number of unique visitors
    return len(visitors)

def main():
    # Read a line of input
    log = input()
    # Get the minimum number of unique visitors
    min_people = get_min_people(log)
    # Print the result
    print(min_people)

if __name__ == '__main__':
    main()

