
def get_max_cookies(n, k, a, b):
    # Initialize variables
    max_cookies = 0
    current_cookies = 0
    current_ingredients = [0] * n

    # Sort the ingredients in descending order
    sorted_ingredients = sorted(range(n), key=lambda i: a[i], reverse=True)

    # Loop through the ingredients and try to make cookies
    for i in sorted_ingredients:
        # Check if we have enough of the current ingredient
        if b[i] >= a[i]:
            # We have enough of the current ingredient, so we can make a cookie
            current_cookies += 1
            current_ingredients[i] += 1
            b[i] -= a[i]
        else:
            # We don't have enough of the current ingredient, so we can't make a cookie
            continue

        # Check if we have enough magic powder left
        if k >= a[i]:
            # We have enough magic powder left, so we can make another cookie
            current_cookies += 1
            current_ingredients[i] += 1
            k -= a[i]
        else:
            # We don't have enough magic powder left, so we can't make another cookie
            break

    # Return the maximum number of cookies we can make
    return current_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

