
import heapq

def combine_ingredients(ingredients):
    heapq.heapify(ingredients)
    while len(ingredients) > 1:
        x = heapq.heappop(ingredients)
        y = heapq.heappop(ingredients)
        new_ingredient = (x + y) / 2
        heapq.heappush(ingredients, new_ingredient)
    return ingredients[0]

if __name__ == "__main__":
    N = int(input())
    values = list(map(int, input().split()))
    ingredients = [-value for value in values]  # Using negative values for max heap
    result = combine_ingredients(ingredients)
    print(-result)  # Convert back to positive value for output
