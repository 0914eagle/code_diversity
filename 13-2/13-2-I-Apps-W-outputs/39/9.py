
def get_max_cookies(n, k, a, b):
    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Initialize the variables
    total_cookies = 0
    current_k = k

    # Iterate through the ingredients
    for ingredient in sorted_ingredients:
        # Check if the current ingredient is enough to make at least one cookie
        if current_k >= ingredient[0]:
            # Calculate the number of cookies that can be made with the current ingredient
            num_cookies = current_k // ingredient[0]
            total_cookies += num_cookies
            current_k -= num_cookies * ingredient[0]
        else:
            # If the current ingredient is not enough to make at least one cookie, break the loop
            break

    return total_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

