
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins for each price
    vitamin_count = {}
    for i in range(n):
        price = prices[i]
        vitamin_count[price] = 0
        for vitamin in vitamins[i]:
            vitamin_count[price] += 1

    # Sort the dictionary by price in ascending order
    sorted_vitamin_count = sorted(vitamin_count.items(), key=lambda x: x[0])

    # Initialize the minimum price and the count of vitamins as 0
    min_price = 0
    total_vitamins = 0

    # Iterate through the dictionary and calculate the minimum price and the count of vitamins
    for price, count in sorted_vitamin_count:
        min_price += price
        total_vitamins += count
        if total_vitamins == 3:
            break

    # If the total count of vitamins is not 3, then return -1
    if total_vitamins != 3:
        return -1

    # Otherwise, return the minimum price
    return min_price

