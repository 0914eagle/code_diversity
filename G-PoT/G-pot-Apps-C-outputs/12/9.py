
n, k = map(int, input().split())
a = list(map(int, input().split()))

total_cows = sum(a)
if total_cows % 2 == 0:
    print("Nicky")
else:
    num_even_piles = sum(1 for x in a if x % 2 == 0)
    if num_even_piles == 0:
        print("Kevin")
    elif num_even_piles % 2 == 0:
        print("Kevin")
    else:
        print("Nicky")
