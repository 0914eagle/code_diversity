
def get_beautiful_array(n, coupons):
    # Initialize an empty array to store the numbers
    array = []
    # Iterate through the coupons
    for coupon in coupons:
        # Extract the number and its cost
        number, cost = coupon
        # If the number is not already in the array, add it
        if number not in array:
            array.append(number)
            # Subtract the cost from the total amount of money
            total_money -= cost
    # Sort the array in ascending order
    array.sort()
    # Return the array and the total amount of money
    return array, total_money

def get_maximum_amount(n, m, coupons):
    # Initialize the total amount of money to 0
    total_money = 0
    # Initialize the maximum amount of money to 0
    maximum_amount = 0
    # Iterate through the coupons
    for coupon in coupons:
        # Extract the number and its cost
        number, cost = coupon
        # Add the cost to the total amount of money
        total_money += cost
        # If the number is not already in the array, add it
        if number not in array:
            array.append(number)
            # Subtract the cost from the total amount of money
            total_money -= cost
    # Sort the array in ascending order
    array.sort()
    # Return the array and the total amount of money
    return array, total_money

if __name__ == '__main__':
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    array, total_money = get_beautiful_array(n, coupons)
    maximum_amount = get_maximum_amount(n, m, coupons)
    print(maximum_amount)

