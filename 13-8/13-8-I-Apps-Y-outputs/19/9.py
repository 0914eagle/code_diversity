
def get_restaurant_menus(n):
    restaurants = []
    for _ in range(n):
        restaurant = input()
        restaurants.append(restaurant)
    return restaurants

def find_restaurant(restaurants):
    for restaurant in restaurants:
        if "pea soup" in restaurant and "pancakes" in restaurant:
            return restaurant
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    n = int(input())
    restaurants = get_restaurant_menus(n)
    print(find_restaurant(restaurants))

