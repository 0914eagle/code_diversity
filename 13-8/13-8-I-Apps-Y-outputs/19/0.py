
def get_menu_items(n):
    menu_items = []
    for _ in range(n):
        menu_items.append(input())
    return menu_items

def find_restaurant(menu_items):
    for restaurant in menu_items:
        if "pea soup" in restaurant and "pancakes" in restaurant:
            return restaurant
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    n = int(input())
    menu_items = get_menu_items(n)
    print(find_restaurant(menu_items))

