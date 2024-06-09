
def get_shortest_test_scheme(k, allergens):
    # Sort the allergens in descending order of their live duration
    allergens = sorted(allergens, reverse=True)
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Loop through each allergen and add its live duration to the number of days needed
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

