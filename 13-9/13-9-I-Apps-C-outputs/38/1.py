
def get_min_distinct_people(sequence):
    # Initialize a set to store the unique visitors
    visitors = set()
    # Iterate through the sequence of characters
    for char in sequence:
        # If the character is "+", add the current visitor to the set
        if char == "+":
            visitors.add(len(visitors))
        # If the character is "-", remove the current visitor from the set
        elif char == "-":
            visitors.remove(len(visitors) - 1)
    # Return the minimum number of distinct people
    return len(visitors)

def main():
    # Read a single line of input from stdin and split it into a list of characters
    sequence = list(input().strip())
    # Get the minimum number of distinct people
    min_distinct_people = get_min_distinct_people(sequence)
    # Print the result
    print(min_distinct_people)

if __name__ == '__main__':
    main()

