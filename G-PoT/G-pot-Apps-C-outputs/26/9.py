
def min_cost_to_ones(n, x, y, a):
    if '0' not in a:
        return 0
    
    cost = 0
    prev = '1'
    for digit in a:
        if digit != prev:
            cost += 1
            prev = digit
    
    return min(cost * y, (cost - 1) * x + y)

# Input parsing
n, x, y = map(int, input().split())
a = input().strip()

# Call the function and print the result
print(min_cost_to_ones(n, x, y, a))
