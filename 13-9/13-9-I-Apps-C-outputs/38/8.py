
def get_min_people(visitor_records):
    # Initialize a set to store the unique visitors
    unique_visitors = set()

    # Iterate through the visitor records
    for record in visitor_records:
        # If the record is '+', add the current visitor to the set
        if record == '+':
            unique_visitors.add(len(unique_visitors))
        # If the record is '-', remove the last added visitor from the set
        elif record == '-':
            unique_visitors.remove(len(unique_visitors) - 1)

    # Return the minimum number of unique visitors
    return len(unique_visitors)

def main():
    # Read the visitor records from stdin
    visitor_records = input()

    # Call the get_min_people function and print the result
    print(get_min_people(visitor_records))

if __name__ == '__main__':
    main()

