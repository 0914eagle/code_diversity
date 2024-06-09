
def solve(n, people):
    # Sort the people by age in ascending order
    people.sort(key=lambda x: x[2])
    # Create a dictionary to map the sex to a title
    titles = {
        "M": "Mr.",
        "F": "Ms."
    }
    # Iterate through the people and print their names in the format requested
    for person in people:
        print(f"{titles[person[3]]} {person[0]} {person[1]}")

