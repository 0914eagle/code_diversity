
def get_distinct_people(visits):
    # Initialize a set to store the distinct people
    distinct_people = set()

    # Iterate through the visit sequence
    for visit in visits:
        # If the visit is "+" (someone entered the club), add their name to the set
        if visit == "+":
            distinct_people.add("Person")
        # If the visit is "-" (someone left the club), remove their name from the set
        elif visit == "-":
            distinct_people.remove("Person")

    # Return the minimum number of distinct people
    return len(distinct_people)

def main():
    # Read a visit sequence from stdin
    visits = input()

    # Call the get_distinct_people function and print the result
    print(get_distinct_people(visits))

if __name__ == '__main__':
    main()

