
def get_number_of_liked_foods(preferences):
    num_people, num_foods = preferences[0]
    foods_liked_by_all = set(range(1, num_foods + 1))
    for person in preferences[1:]:
        foods_liked_by_person = set(person)
        foods_liked_by_all = foods_liked_by_all.intersection(foods_liked_by_person)
    return len(foods_liked_by_all)

