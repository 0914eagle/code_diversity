
def get_restaurant_menus(n):
    restaurant_menus = []
    for _ in range(n):
        k = int(input())
        menu = []
        for _ in range(k + 1):
            menu.append(input())
        restaurant_menus.append(menu)
    return restaurant_menus

def find_restaurant(restaurant_menus):
    for restaurant in restaurant_menus:
        if "pea soup" in restaurant and "pancakes" in restaurant:
            return restaurant[0]
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    n = int(input())
    restaurant_menus = get_restaurant_menus(n)
    print(find_restaurant(restaurant_menus))

