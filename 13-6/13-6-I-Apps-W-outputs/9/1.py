
def solve(n):
    lucky_digits = ["4", "7"]
    lucky_numbers = []
    for i in range(1, n+1):
        if set(str(i)).issubset(lucky_digits):
            lucky_numbers.append(i)
    return lucky_numbers.index(n)+1
