
def get_menu_items(menu_list):
    menu_items = []
    for menu in menu_list:
        menu_items.extend(menu.split())
    return menu_items

def find_restaurant(menu_list):
    menu_items = get_menu_items(menu_list)
    for restaurant in menu_list:
        if "pea soup" in menu_items and "pancakes" in menu_items:
            return restaurant
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    num_restaurants = int(input())
    menu_list = []
    for _ in range(num_restaurants):
        num_menu_items = int(input())
        menu_items = input().split()
        menu_list.append(" ".join(menu_items))
    print(find_restaurant(menu_list))

