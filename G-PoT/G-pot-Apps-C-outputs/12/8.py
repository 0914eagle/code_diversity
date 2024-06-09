
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Count the number of piles with even number of cows
even_piles = sum(1 for x in a if x % 2 == 0)

# If there are no even piles, Nicky wins
if even_piles == 0:
    print("Nicky")
# If there is only one pile and it has even number of cows, Kevin wins
elif n == 1 and a[0] % 2 == 0:
    print("Kevin")
# If there is only one pile and it has odd number of cows, Nicky wins
elif n == 1 and a[0] % 2 != 0:
    print("Nicky")
# If there are multiple piles and the total number of cows is even, Kevin wins
elif sum(a) % 2 == 0:
    print("Kevin")
# If there are multiple piles and the total number of cows is odd, Nicky wins
else:
    print("Nicky")
