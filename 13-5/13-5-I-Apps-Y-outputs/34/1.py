
def get_restaurants(n):
    restaurants = []
    for i in range(n):
        city, score = input().split()
        restaurants.append((city, int(score)))
    return restaurants

def get_sorted_restaurants(restaurants):
    return sorted(restaurants, key=lambda x: (x[0], -x[1]))

def get_identification_numbers(restaurants):
    return [str(i+1) for i in range(len(restaurants))]

def main():
    n = int(input())
    restaurants = get_restaurants(n)
    sorted_restaurants = get_sorted_restaurants(restaurants)
    identification_numbers = get_identification_numbers(sorted_restaurants)
    for identification_number in identification_numbers:
        print(identification_number)

if __name__ == '__main__':
    main()

