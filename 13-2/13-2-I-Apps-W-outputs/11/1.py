
def is_hq9_plus(code):
    return "HQ" in code and "Q" in code and len(code) <= 10**6

