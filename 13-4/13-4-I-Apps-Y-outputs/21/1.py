
def get_moose_points(left_tines, right_tines):
    if left_tines == right_tines:
        return f"Even {left_tines * 2}"
    else:
        return f"Odd {max(left_tines, right_tines) * 2}"

