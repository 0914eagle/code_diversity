
def get_ingredients():
    N = int(input())
    ingredients = []
    for i in range(N):
        ingredients.append(float(input()))
    return ingredients

def compose_ingredients(ingredients):
    while len(ingredients) > 1:
        ingredients = [sum(ingredients[i:i+2])/2 for i in range(0, len(ingredients), 2)]
    return ingredients[0]

def main():
    ingredients = get_ingredients()
    print(compose_ingredients(ingredients))

if __name__ == '__main__':
    main()

