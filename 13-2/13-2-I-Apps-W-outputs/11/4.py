
def is_valid_hq9_plus(code):
    return "HQ" in code and code.count("H") % 2 == 0 and code.count("Q") % 2 == 0

