
def get_max_cookies(n, k, a, b):
    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Initialize the variables
    current_cookies = 0
    current_weight = 0

    # Iterate through the ingredients
    for ingredient, weight in sorted_ingredients:
        # Check if the current weight plus the weight of the current ingredient is less than or equal to the magic powder
        if current_weight + weight <= k:
            # Add the current ingredient to the current weight
            current_weight += weight
            # Increment the number of cookies
            current_cookies += 1
        else:
            # Calculate the number of cookies that can be made with the current weight
            current_cookies += current_weight // ingredient
            # Break the loop
            break

    # Return the maximum number of cookies
    return current_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

