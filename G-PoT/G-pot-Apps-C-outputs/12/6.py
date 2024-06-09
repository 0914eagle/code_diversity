
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Check if the total number of cows is odd
total_cows = sum(a)
if total_cows % 2 == 1:
    print("Kevin")
else:
    # Check if there is at least one pile with odd number of cows
    if any(x % 2 == 1 for x in a):
        print("Nicky")
    else:
        # Check if k is odd
        if k % 2 == 1:
            print("Kevin")
        else:
            print("Nicky")
