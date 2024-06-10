
def get_menu_items(n):
    menu_items = []
    for _ in range(n):
        menu_item = input()
        menu_items.append(menu_item)
    return menu_items

def check_menu_items(menu_items):
    for menu_item in menu_items:
        if "pea soup" in menu_item and "pancakes" in menu_item:
            return True
    return False

def get_restaurant_name(menu_items):
    for menu_item in menu_items:
        if "pea soup" in menu_item and "pancakes" in menu_item:
            return menu_item.split()[0]
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    n = int(input())
    menu_items = get_menu_items(n)
    if check_menu_items(menu_items):
        print(get_restaurant_name(menu_items))
    else:
        print(get_restaurant_name(menu_items))

