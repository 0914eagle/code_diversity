
def get_pizzas(n, a):
    # Initialize variables
    total_pizzas = 0
    coupon_used = False
    discount_used = False
    
    # Iterate through the number of days
    for i in range(n):
        # Check if there are any teams present on this day
        if a[i] > 0:
            # Check if a coupon can be used
            if not coupon_used and a[i] >= 2:
                total_pizzas += 1
                coupon_used = True
            # Check if a discount can be used
            elif not discount_used and a[i] >= 1:
                total_pizzas += 2
                discount_used = True
            # If no coupon or discount can be used, buy one pizza
            else:
                total_pizzas += 1
    
    # Check if the total number of pizzas is correct
    if total_pizzas == sum(a):
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_pizzas(n, a))

if __name__ == '__main__':
    main()

