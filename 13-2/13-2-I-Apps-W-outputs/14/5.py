
def is_power_of_three_and_five(n):
    for i in range(1, n):
        if n == 3**i + 5**i:
            return True
    return False

n = int(input())
if is_power_of_three_and_five(n):
    print(-1)
else:
    for i in range(1, n):
        if n == 3**i + 5**i:
            print(i, n-i)
            break

