
def get_restaurant_info(n):
    restaurant_info = []
    for i in range(n):
        restaurant_name, score = input().split()
        restaurant_info.append((restaurant_name, int(score)))
    return restaurant_info

def sort_restaurants(restaurant_info):
    return sorted(restaurant_info, key=lambda x: (x[0], -x[1]))

def print_restaurant_ids(restaurant_info):
    for i, (restaurant_name, score) in enumerate(restaurant_info, start=1):
        print(i)

if __name__ == '__main__':
    n = int(input())
    restaurant_info = get_restaurant_info(n)
    sorted_restaurant_info = sort_restaurants(restaurant_info)
    print_restaurant_ids(sorted_restaurant_info)

