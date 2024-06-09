
def get_liked_foods(people):
    num_people, num_foods = len(people), len(people[0])
    liked_foods = [set(people[0])]
    for i in range(1, num_people):
        liked_foods.append(set(people[i]))
        liked_foods[0] &= liked_foods[i]
    return len(liked_foods[0])

