
def get_sorted_restaurants(n, restaurants):
    return sorted(restaurants, key=lambda x: (x[0], -x[1]))

def get_restaurant_ids(n, restaurants):
    return [i for i, _ in restaurants]

def main():
    n = int(input())
    restaurants = []
    for _ in range(n):
        city, score = input().split()
        restaurants.append((city, int(score)))
    sorted_restaurants = get_sorted_restaurants(n, restaurants)
    restaurant_ids = get_restaurant_ids(n, sorted_restaurants)
    for i in restaurant_ids:
        print(i)

if __name__ == '__main__':
    main()

