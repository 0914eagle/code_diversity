
def solve(people):
    # sort the people by age in ascending order
    people.sort(key=lambda x: x[2])
    # create a dictionary to map sex to a title
    titles = {
        "M": "Mr.",
        "F": "Ms."
    }
    # iterate through the people and print their names in the format specified
    for person in people:
        print(f"{titles[person[3]]} {person[0]} {person[1]}")

