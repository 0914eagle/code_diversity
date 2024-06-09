
def solve(people):
    # Sort the people by age in ascending order
    people.sort(key=lambda x: x[2])
    # Create a dictionary to map each sex to a title
    titles = {"M": "Mr.", "F": "Ms."}
    # Iterate over the people and print their names in the required format
    for person in people:
        first_name, last_name, age, sex = person
        print(f"{titles[sex]}{last_name}, {first_name}")
    return people

