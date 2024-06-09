
def solve(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills for each denomination
    bills = {}
    for i in range(n):
        bills[a[i]] = 0

    # Loop through each request and calculate the minimum number of bills needed
    for i in range(q):
        # Initialize the minimum number of bills needed to the maximum possible (k)
        min_bills = k
        # Loop through each denomination and calculate the number of bills needed for the current request
        for j in range(n):
            # If the current denomination is less than or equal to the current request, increment the number of bills needed for that denomination
            if a[j] <= x[i]:
                bills[a[j]] += 1
                # If the number of bills needed for the current denomination is less than the minimum number of bills needed, update the minimum number of bills needed
                if bills[a[j]] < min_bills:
                    min_bills = bills[a[j]]
        # If the minimum number of bills needed is greater than the maximum number of bills available, print -1, otherwise print the minimum number of bills needed
        if min_bills > k:
            print(-1)
        else:
            print(min_bills)

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

solve(n, k, a, q, x)

