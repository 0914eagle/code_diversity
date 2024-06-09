
def get_shortest_test_scheme(k, allergens):
    # Sort the allergens by their live duration in descending order
    allergens = sorted(allergens, reverse=True)
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Loop through each allergen and add its live duration to the number of days needed for the test scheme
    for allergen in allergens:
        num_days += allergen
    
    return num_days

def main():
    k = int(input())
    allergens = []
    for i in range(k):
        allergens.append(int(input()))
    print(get_shortest_test_scheme(k, allergens))

if __name__ == '__main__':
    main()

