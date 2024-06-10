
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of occurrences of each number
    num_occurrences = {}
    for coupon in coupons:
        q, w = coupon
        if q not in num_occurrences:
            num_occurrences[q] = 1
        else:
            num_occurrences[q] += 1
    
    # Initialize a list to store the maximum amount of money that can be paid for each number
    max_amount = [0] * (n + 1)
    max_amount[0] = 0
    
    # Loop through the numbers in the dictionary and calculate the maximum amount of money that can be paid for each number
    for num in num_occurrences:
        max_amount[num_occurrences[num]] = max(max_amount[num_occurrences[num] - 1], max_amount[num_occurrences[num] - 2] + num * num_occurrences[num])
    
    # Return the maximum amount of money that can be paid
    return max_amount[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

