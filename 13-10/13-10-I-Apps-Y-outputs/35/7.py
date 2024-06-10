
def get_ingredients(N):
    ingredients = []
    for i in range(N):
        ingredients.append(float(input()))
    return ingredients

def compose_ingredients(ingredients):
    if len(ingredients) == 1:
        return ingredients[0]
    else:
        ingredients.sort(reverse=True)
        ingredients = [sum(ingredients[0:2])/2] + ingredients[2:]
        return compose_ingredients(ingredients)

def main():
    N = int(input())
    ingredients = get_ingredients(N)
    print(compose_ingredients(ingredients))

if __name__ == '__main__':
    main()

