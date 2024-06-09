
def get_moose_points(left, right):
    if left == right:
        return f"Even {left + right}"
    else:
        return f"Odd {max(left, right) * 2}"

