
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupon uses for each number
    coupon_uses = {}
    for q, w in coupons:
        if q not in coupon_uses:
            coupon_uses[q] = 0
        coupon_uses[q] += 1

    # Initialize a set to store the numbers that have been used
    used_numbers = set()

    # Initialize a variable to store the maximum amount paid
    maximum_amount = 0

    # Iterate through the numbers 1 to n
    for i in range(1, n + 1):
        # If the number has not been used and there are coupons available for it
        if i not in used_numbers and coupon_uses.get(i, 0) > 0:
            # Use the coupon for the number and add the cost to the maximum amount paid
            maximum_amount += i
            used_numbers.add(i)
            coupon_uses[i] -= 1

            # If the maximum amount paid is equal to the total cost of all coupons
            if maximum_amount == sum(w for q, w in coupons):
                # Return the maximum amount paid
                return maximum_amount

    # If no optimal solution is found, return 0
    return 0

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

