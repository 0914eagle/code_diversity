
def get_max_cookies(n, k, a, b):
    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Initialize the variables
    current_cookies = 0
    current_weight = 0

    # Iterate through the ingredients
    for i in range(n):
        # Calculate the number of cookies that can be baked with the current ingredient
        num_cookies = min(sorted_ingredients[i][1], k // sorted_ingredients[i][0])

        # Update the current weight and number of cookies
        current_weight += num_cookies * sorted_ingredients[i][0]
        current_cookies += num_cookies

        # Check if the current weight is greater than the total weight
        if current_weight > k:
            break

    # Return the maximum number of cookies that can be baked
    return current_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

