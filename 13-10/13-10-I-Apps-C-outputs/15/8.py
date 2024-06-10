
def get_maximum_payment(n, m, coupons):
    # Initialize a dictionary to store the number of times each number appears in the array
    number_counts = {}
    for coupon in coupons:
        q, w = coupon
        if q not in number_counts:
            number_counts[q] = 0
        number_counts[q] += 1
    
    # Initialize a dictionary to store the maximum payment for each number
    maximum_payments = {}
    for q, count in number_counts.items():
        maximum_payments[q] = count * w
    
    # Iterate through the array and find the maximum payment for each number
    for i in range(n - 1):
        for j in range(i + 1, n):
            q1, q2 = a[i], a[j]
            if q1 != q2:
                maximum_payments[q1] = max(maximum_payments[q1], maximum_payments[q2] + w)
                maximum_payments[q2] = max(maximum_payments[q2], maximum_payments[q1] + w)
    
    # Return the maximum payment for the last number in the array
    return maximum_payments[a[n - 1]]

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_payment(n, m, coupons))

if __name__ == '__main__':
    main()

