
def get_input():
    N = int(input())
    restaurants = []
    for i in range(N):
        restaurant = input().split()
        restaurants.append((restaurant[0], int(restaurant[1])))
    return restaurants

def sort_restaurants(restaurants):
    return sorted(restaurants, key=lambda x: (x[0], -x[1]))

def print_output(restaurants):
    for i, restaurant in enumerate(restaurants, 1):
        print(i)

if __name__ == '__main__':
    restaurants = get_input()
    sorted_restaurants = sort_restaurants(restaurants)
    print_output(sorted_restaurants)

