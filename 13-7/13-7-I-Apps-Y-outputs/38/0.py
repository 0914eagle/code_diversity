
def name_directory(people):
    # Sort the people by age and then by last name
    people = sorted(people, key=lambda x: (x[2], x.lower()))
    # Create a dictionary to map each person's sex to a title
    titles = {
        "M": "Mr.",
        "F": "Ms.",
    }
    # Create a list to store the formatted names
    formatted_names = []
    for person in people:
        # Extract the first name, last name, and sex from the person's information
        first_name, last_name, sex = person[0], person[1], person[3]
        # Create the formatted name using the title and the first and last names
        formatted_name = titles[sex] + " " + first_name + " " + last_name
        formatted_names.append(formatted_name)
    return formatted_names

