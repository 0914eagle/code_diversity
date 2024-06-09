
def get_max_cookies(n, k, a, b):
    # Initialize variables
    max_cookies = 0
    current_cookies = 0
    current_powder = k

    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Iterate through the ingredients and calculate the maximum number of cookies that can be baked
    for ingredient in sorted_ingredients:
        if current_powder == 0:
            break
        if ingredient[1] <= current_powder:
            current_cookies += ingredient[0]
            current_powder -= ingredient[1]
        else:
            current_cookies += current_powder // ingredient[1] * ingredient[0]
            current_powder %= ingredient[1]
        max_cookies = max(max_cookies, current_cookies)

    return max_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

