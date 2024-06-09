
def get_maximum_taste(fruits, k):
    total_taste = sum([fruit[0] for fruit in fruits])
    total_calories = sum([fruit[1] for fruit in fruits])
    if total_taste == 0 or total_calories == 0:
        return -1
    taste_ratio = total_taste / total_calories
    if taste_ratio == k:
        return total_taste
    elif taste_ratio > k:
        return -1
    else:
        fruits.sort(key=lambda x: x[0] / x[1], reverse=True)
        chosen_fruits = []
        current_taste = 0
        current_calories = 0
        for fruit in fruits:
            current_taste += fruit[0]
            current_calories += fruit[1]
            chosen_fruits.append(fruit)
            if current_taste / current_calories == k:
                return current_taste
        return -1

