
def get_liked_foods(preferences):
    # Initialize a set to store the foods liked by all people
    liked_foods = set(range(1, len(preferences[0]) + 1))
    for person in preferences:
        # Iterate over the person's preferences and remove the foods they don't like
        for food in range(1, len(person) + 1):
            if food not in person:
                liked_foods.discard(food)
    return len(liked_foods)

