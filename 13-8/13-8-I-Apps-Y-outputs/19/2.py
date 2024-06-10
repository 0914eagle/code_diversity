
def get_restaurant_menus(n):
    restaurants = []
    for _ in range(n):
        num_items = int(input())
        menu_items = []
        for _ in range(num_items):
            menu_item = input()
            menu_items.append(menu_item)
        restaurants.append(menu_items)
    return restaurants

def find_restaurant(restaurants):
    for restaurant in restaurants:
        if "pea soup" in restaurant and "pancakes" in restaurant:
            return restaurant[0]
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    n = int(input())
    restaurants = get_restaurant_menus(n)
    print(find_restaurant(restaurants))

