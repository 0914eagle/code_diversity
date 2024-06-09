
def get_max_cookies(n, k, a, b):
    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Initialize the variables
    total_cookies = 0
    current_powder = k

    # Loop through the ingredients
    for ingredient in sorted_ingredients:
        # Check if the current ingredient is enough to bake a cookie
        if ingredient[1] <= current_powder:
            # Bake a cookie and update the variables
            total_cookies += 1
            current_powder -= ingredient[1]
        else:
            # Break the loop if the current ingredient is not enough to bake a cookie
            break

    # Return the maximum number of cookies that can be baked
    return total_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

