
def solve(q, a, b, c):
    # Find the maximum number of candies Alice can have after the division
    max_candies = max(a, b, c)
    
    # If Alice has more candies than Bob, she discards some candies so that the number of candies she has is equal to the number of candies Bob has
    if a > b:
        a = b
    if b > c:
        b = c
    
    # Return the maximum number of candies Alice can have after the division
    return max_candies

q = int(input())

for i in range(q):
    a, b, c = map(int, input().split())
    print(solve(q, a, b, c))

