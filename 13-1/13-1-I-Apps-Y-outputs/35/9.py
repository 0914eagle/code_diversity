
def max_profit(n, k, a):
    # Sort the difficulties in descending order
    a.sort(reverse=True)
    # Initialize the total profit and the number of problems solved each day
    total_profit, num_problems = 0, 0
    # Loop through the days
    for i in range(k):
        # Add the maximum difficulty of the problems solved each day to the total profit
        total_profit += a[num_problems]
        # Increment the number of problems solved each day
        num_problems += 1
    # Return the total profit and the number of problems solved each day
    return total_profit, num_problems

n, k = map(int, input().split())
a = list(map(int, input().split()))
total_profit, num_problems = max_profit(n, k, a)
print(total_profit)
print(*[num_problems] * k)

