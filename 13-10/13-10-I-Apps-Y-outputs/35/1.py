
def read_input():
    N = int(input())
    ingredients = [int(x) for x in input().split()]
    return N, ingredients

def find_max_value(ingredients):
    max_value = 0
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)):
            max_value = max(max_value, (ingredients[i] + ingredients[j]) / 2)
    return max_value

def main():
    N, ingredients = read_input()
    print(find_max_value(ingredients))

if __name__ == '__main__':
    main()

