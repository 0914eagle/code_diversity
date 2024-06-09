
N = int(input())

# Probability of at least one person giving a gift to themselves
# P(at least one person gives gift to themselves) = 1 - P(no one gives gift to themselves)
# P(no one gives gift to themselves) = N! / N^N
# P(at least one person gives gift to themselves) = 1 - N! / N^N

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

probability = 1 - factorial(N) / (N ** N)
print("{:.8f}".format(probability))
