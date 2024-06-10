
def get_minimum_number_of_people(visits):
    # Initialize a set to store the unique visits
    unique_visits = set()

    # Iterate through the visits
    for visit in visits:
        # If the visit is '+', add it to the set of unique visits
        if visit == "+":
            unique_visits.add(visit)
        # If the visit is '-', remove it from the set of unique visits
        elif visit == "-":
            unique_visits.remove(visit)

    # Return the length of the set of unique visits
    return len(unique_visits)

def main():
    # Read a line of input from stdin and split it into a list of characters
    visits = list(input().strip())

    # Call the get_minimum_number_of_people function and print the result
    print(get_minimum_number_of_people(visits))

if __name__ == "__main__":
    main()

