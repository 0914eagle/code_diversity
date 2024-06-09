
def get_liked_foods(num_people, num_foods, people_answers):
    liked_foods = set(range(1, num_foods+1))
    for person_answers in people_answers:
        liked_foods = liked_foods.intersection(set(person_answers))
    return len(liked_foods)

