
def solve(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills required for each sum
    bills_required = {}

    # Loop through the denominations and calculate the maximum sum that can be obtained with each denomination
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += a[k]
                if sum > x[0]:
                    break
            bills_required[sum] = j - i + 1

    # Loop through the requests and check if the sum can be obtained with the maximum number of bills
    for i in range(q):
        if bills_required.get(x[i]) <= k:
            print(bills_required[x[i]])
        else:
            print(-1)

solve(6, 20, [10, 50, 100, 500, 1000, 5000], 8, [4200, 100000, 95000, 96000, 99000, 10100, 2015, 9950])

