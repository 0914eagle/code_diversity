
def get_ingredients():
    N = int(input())
    ingredients = []
    for i in range(N):
        ingredients.append(float(input()))
    return ingredients

def get_max_value(ingredients):
    if len(ingredients) == 1:
        return ingredients[0]
    else:
        return max(ingredients[0] + ingredients[1], get_max_value(ingredients[1:]))

if __name__ == '__main__':
    ingredients = get_ingredients()
    print(get_max_value(ingredients))

