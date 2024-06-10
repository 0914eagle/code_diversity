
def get_pizzas(n, a):
    # Initialize variables
    coupon_count = 0
    discount_count = 0
    pizzas_needed = a[0]

    # Iterate over the number of days
    for i in range(1, n):
        # If there are more teams on the current day than on the previous day, use a coupon
        if a[i] > a[i-1]:
            coupon_count += 1
        # If there are more teams on the current day than on the previous day and the previous day was not the first day, use a discount
        elif a[i] > a[i-1] and i > 1:
            discount_count += 1
        # If there are the same number of teams on the current day as on the previous day, use neither a coupon nor a discount
        else:
            pass
        # Update the number of pizzas needed for the current day
        pizzas_needed += a[i]

    # Check if the number of pizzas needed is less than or equal to the total number of pizzas that can be bought with the available coupons and discounts
    if pizzas_needed <= (coupon_count * 2) + discount_count:
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_pizzas(n, a))

if __name__ == '__main__':
    main()

