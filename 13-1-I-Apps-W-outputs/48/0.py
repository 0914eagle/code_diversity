
def solve(categories, statement):
    # Initialize a dictionary to store the number of matches for each category
    matches = {}

    # Iterate over the categories
    for category in categories:
        # Initialize the number of matches for this category to 0
        matches[category] = 0

        # Iterate over the words in the statement
        for word in statement:
            # Check if the word is in the category's associated words
            if word in categories[category]:
                # Increment the number of matches for this category
                matches[category] += 1

    # Find the category with the highest number of matches
    max_matches = max(matches.values())

    # Initialize a list to store the categories with the highest number of matches
    highest_categories = []

    # Iterate over the categories and their matches
    for category, num_matches in matches.items():
        # Check if the category has the highest number of matches
        if num_matches == max_matches:
            # Add the category to the list of categories with the highest number of matches
            highest_categories.append(category)

    # Sort the list of categories in lexicographical order
    highest_categories.sort()

    # Return the list of categories with the highest number of matches
    return highest_categories

