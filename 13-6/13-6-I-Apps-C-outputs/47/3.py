
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the counts of each number
    counts = {}
    for coupon in coupons:
        q, w = coupon
        if q not in counts:
            counts[q] = 0
        counts[q] += 1
    
    # Initialize a variable to store the maximum amount
    maximum_amount = 0
    
    # Iterate over the counts and calculate the maximum amount
    for q, count in counts.items():
        maximum_amount += count * q
    
    return maximum_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    maximum_amount = get_maximum_amount(n, m, coupons)
    print(maximum_amount)

if __name__ == '__main__':
    main()

