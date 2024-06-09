
def get_min_unfortunate_sum(n, a):
    # Sort the banknote values in descending order
    a.sort(reverse=True)
    # Initialize the minimum unfortunate sum as the largest banknote value
    min_sum = a[0]
    # Iterate through the banknote values and check if they can be used to form an unfortunate sum
    for i in range(1, n):
        if a[i] > min_sum:
            break
        min_sum += a[i]
    # If all banknote values are less than or equal to the minimum unfortunate sum, there are no unfortunate sums
    if min_sum > a[-1]:
        return -1
    else:
        return min_sum

n = int(input())
a = list(map(int, input().split()))
print(get_min_unfortunate_sum(n, a))

