
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
            k -= 1
        else:
            # We don't have enough of the current ingredient, so we can't make a cookie
            pass

        # Check if we have used up all of the magic powder
        if k == 0:
            # We have used up all of the magic powder, so we can stop making cookies
            break

    # Return the maximum number of cookies we can make
    return current_cookies

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

if __name__ == '__main__':
    main()

