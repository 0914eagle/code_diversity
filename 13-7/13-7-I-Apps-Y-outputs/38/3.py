
def solve(people):
    # Sort the people by age and name
    people.sort(key=lambda x: (x[2], x.lower()))
    # Create a dictionary to map sex to title
    titles = {"M": "Mr.", "F": "Ms."}
    # Iterate over the people and print their names in the format specified
    for person in people:
        print(f"{titles[person[3]]} {person[0]} {person[1]}")

