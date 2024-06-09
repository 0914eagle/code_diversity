
def atm(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills required for each sum
    bills_required = {}

    # Loop through the denominations and calculate the number of bills required for each sum
    for i in range(n):
        for j in range(i, n):
            current_sum = a[i] * 10 ** i + a[j] * 10 ** j
            if current_sum <= x[0]:
                bills_required[current_sum] = 1
            elif current_sum <= x[1]:
                bills_required[current_sum] = 2
            else:
                bills_required[current_sum] = -1

    # Loop through the requests for cash withdrawal and print the minimum number of bills required for each sum
    for i in range(q):
        if bills_required[x[i]] != -1:
            print(bills_required[x[i]])
        else:
            print(-1)

atm(6, 20, [10, 50, 100, 500, 1000, 5000], 8, [4200, 100000, 95000, 96000, 99000, 10100, 2015, 9950])

