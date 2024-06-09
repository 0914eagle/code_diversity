
def get_restaurants(n):
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append((city, int(score)))
    return restaurants

def sort_restaurants(restaurants):
    return sorted(restaurants, key=lambda x: (x[0], -x[1]))

def print_restaurants(restaurants):
    for i, (city, score) in enumerate(restaurants, start=1):
        print(i)

if __name__ == '__main__':
    n = int(input())
    restaurants = get_restaurants(n)
    sorted_restaurants = sort_restaurants(restaurants)
    print_restaurants(sorted_restaurants)

