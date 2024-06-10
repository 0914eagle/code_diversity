
def find_restaurant(menus):
    # Initialize a dictionary to store the menu items for each restaurant
    restaurant_menu_items = {}
    
    # Iterate over the menus
    for menu in menus:
        # Split the menu into lines
        lines = menu.splitlines()
        
        # Get the restaurant name and menu items
        restaurant_name = lines[0]
        menu_items = lines[1:]
        
        # Add the menu items to the dictionary
        restaurant_menu_items[restaurant_name] = menu_items
    
    # Find the restaurant with both "pea soup" and "pancakes" as menu items
    for restaurant, menu_items in restaurant_menu_items.items():
        if "pea soup" in menu_items and "pancakes" in menu_items:
            return restaurant
    
    # If no restaurant has both "pea soup" and "pancakes" as menu items, return "Anywhere is fine I guess"
    return "Anywhere is fine I guess"

def main():
    # Read the input from stdin
    n = int(input())
    menus = [input() for _ in range(n)]
    
    # Find the restaurant with both "pea soup" and "pancakes" as menu items
    restaurant = find_restaurant(menus)
    
    # Print the result
    print(restaurant)

if __name__ == '__main__':
    main()

