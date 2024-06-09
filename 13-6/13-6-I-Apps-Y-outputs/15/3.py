
def get_liked_foods(preferences):
    num_people, num_foods = preferences[0]
    liked_foods = set(range(1, num_foods + 1))
    for person in preferences[1:]:
        liked_foods = liked_foods.intersection(set(person))
    return len(liked_foods)

