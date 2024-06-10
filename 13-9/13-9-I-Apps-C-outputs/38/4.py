
def get_minimum_people(visitor_record):
    # Initialize a set to store the unique visitors
    unique_visitors = set()

    # Iterate through the visitor record
    for visitor in visitor_record:
        # If the visitor is entering the club, add them to the set
        if visitor == "+":
            unique_visitors.add(visitor)
        # If the visitor is leaving the club, remove them from the set
        elif visitor == "-":
            unique_visitors.remove(visitor)

    # Return the minimum number of unique visitors
    return len(unique_visitors)

def main():
    # Read a line of input from stdin and split it into a list of characters
    visitor_record = list(input().strip())

    # Call the get_minimum_people function and print the result
    print(get_minimum_people(visitor_record))

if __name__ == '__main__':
    main()

