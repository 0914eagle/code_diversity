
def solve(people):
    # Sort the people by age and then by last name
    people.sort(key=lambda x: (x[2], x[1]))
    # Create a dictionary to map sex to title
    titles = {"M": "Mr.", "F": "Ms."}
    # Iterate through the people and print their names in the format requested
    for person in people:
        print(f"{titles[person[3]]} {person[0]} {person[1]}")
    return people

