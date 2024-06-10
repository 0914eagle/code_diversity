
def get_maximum_number_of_favorite_drinks(n, k, favorite_drinks):
    # Initialize a dictionary to store the number of favorite drinks for each student
    favorite_drinks_count = {}
    for i in range(n):
        favorite_drinks_count[i] = 0
    
    # Iterate over the favorite drinks of each student and increment the count for that drink
    for i in range(n):
        favorite_drinks_count[favorite_drinks[i] - 1] += 1
    
    # Initialize a list to store the maximum number of favorite drinks that can be gained
    max_favorite_drinks = []
    
    # Iterate over the dictionary and find the maximum number of favorite drinks that can be gained
    for i in range(k):
        max_favorite_drinks.append(max(favorite_drinks_count.values()))
    
    # Return the maximum number of favorite drinks that can be gained
    return sum(max_favorite_drinks)

def main():
    n, k = map(int, input().split())
    favorite_drinks = []
    for i in range(n):
        favorite_drinks.append(int(input()))
    print(get_maximum_number_of_favorite_drinks(n, k, favorite_drinks))

if __name__ == '__main__':
    main()

