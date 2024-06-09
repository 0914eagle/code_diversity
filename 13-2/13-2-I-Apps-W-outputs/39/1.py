
def get_max_cookies(n, k, a, b):
    # Sort the ingredients in descending order
    sorted_ingredients = sorted(zip(a, b), key=lambda x: x[1], reverse=True)

    # Initialize the variables
    total_cookies = 0
    current_weight = 0

    # Iterate through the ingredients
    for i in range(n):
        # Calculate the current weight
        current_weight += sorted_ingredients[i][1]

        # Check if the current weight is less than or equal to the magic powder
        if current_weight <= k:
            # Add the current cookie to the total
            total_cookies += 1
        else:
            # Calculate the number of cookies that can be made with the current weight
            total_cookies += int(current_weight / k)
            break

    return total_cookies

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_cookies(n, k, a, b))

