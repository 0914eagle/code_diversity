
def solve(a):
    a_str = str(a)
    digits = [int(i) for i in a_str if i in "1689"]
    if len(digits) < 4:
        return 0
    digits.sort(reverse=True)
    result = int("".join(map(str, digits)))
    if result % 7 == 0:
        return result
    else:
        return 0

