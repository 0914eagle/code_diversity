
def solve(people):
    # Sort the people by age in ascending order
    people.sort(key=lambda x: x[2])
    # Create a dictionary to map sex to title
    titles = {"M": "Mr.", "F": "Ms."}
    # Iterate over the people and print their names in the format requested
    for person in people:
        print(f"{titles[person[3]]} {person[0]} {person[1]}")
    return people

