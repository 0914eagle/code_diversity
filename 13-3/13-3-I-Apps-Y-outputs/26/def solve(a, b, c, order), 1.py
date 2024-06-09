
def solve(a, b, c, order):
    nums = [a, b, c]
    return " ".join(str(nums[order.index(c1)]) for c1 in order)

