
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the counts of each number
    counts = {}
    for coupon in coupons:
        q, w = coupon
        if q not in counts:
            counts[q] = 0
        counts[q] += 1
    
    # Initialize a list to store the numbers that can be used to form pairs
    numbers = []
    for q, count in counts.items():
        if count % 2 == 1:
            numbers.append(q)
    
    # Initialize a variable to store the maximum amount that can be paid
    maximum_amount = 0
    
    # Iterate over all possible pairs of numbers
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            q1 = numbers[i]
            q2 = numbers[j]
            w1 = counts[q1]
            w2 = counts[q2]
            amount = w1 * w2
            if amount > maximum_amount:
                maximum_amount = amount
    
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

