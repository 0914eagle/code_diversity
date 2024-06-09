
def get_ingredients():
    N = int(input())
    ingredients = []
    for i in range(N):
        ingredients.append(int(input()))
    return ingredients

def compose_ingredients(ingredients):
    while len(ingredients) > 1:
        ingredients.append((ingredients.pop() + ingredients.pop()) / 2)
    return ingredients[0]

def main():
    ingredients = get_ingredients()
    print(compose_ingredients(ingredients))

if __name__ == '__main__':
    main()

