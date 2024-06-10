
def get_restaurant_menus():
    n = int(input())
    restaurants = []
    for i in range(n):
        k = int(input())
        restaurant = {}
        restaurant["name"] = input()
        restaurant["menu"] = []
        for j in range(k):
            restaurant["menu"].append(input())
        restaurants.append(restaurant)
    return restaurants

def decide_where_to_eat(restaurants):
    for restaurant in restaurants:
        if "pea soup" in restaurant["menu"] and "pancakes" in restaurant["menu"]:
            return restaurant["name"]
    return "Anywhere is fine I guess"

if __name__ == '__main__':
    restaurants = get_restaurant_menus()
    print(decide_where_to_eat(restaurants))

