
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of occurrences of each number
    number_counts = {}
    for q, w in coupons:
        if q not in number_counts:
            number_counts[q] = 0
        number_counts[q] += 1
    
    # Initialize a list to store the maximum amount of money that can be paid for each number
    max_amounts = [0] * (n + 1)
    max_amounts[0] = 0
    
    # Loop through each number and calculate the maximum amount of money that can be paid for it
    for i in range(1, n + 1):
        if i in number_counts:
            max_amounts[i] = max(max_amounts[i - 1], max_amounts[i - number_counts[i]] + number_counts[i] * coupons[(i, i)][1])
        else:
            max_amounts[i] = max_amounts[i - 1]
    
    return max_amounts[n]

def main():
    n, m = map(int, input().split())
    coupons = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

