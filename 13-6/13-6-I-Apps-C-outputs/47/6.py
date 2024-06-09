
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons used for each value
    counts = {}
    for q, w in coupons:
        counts[q] = counts.get(q, 0) + 1

    # Initialize a set to store the values that have been used
    used_values = set()

    # Initialize a variable to store the maximum amount paid
    maximum_amount = 0

    # Loop through the values 1 to n
    for i in range(1, n + 1):
        # If the value has not been used and there are coupons available for it
        if i not in used_values and counts.get(i, 0) > 0:
            # Use the value and deduct the cost of the coupon from the maximum amount paid
            used_values.add(i)
            maximum_amount -= counts[i]

            # If the value has been used and there are coupons available for it
        elif i in used_values and counts.get(i + 1, 0) > 0:
            # Use the value and deduct the cost of the coupon from the maximum amount paid
            used_values.remove(i)
            maximum_amount -= counts[i + 1]

    # Return the maximum amount paid
    return maximum_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

