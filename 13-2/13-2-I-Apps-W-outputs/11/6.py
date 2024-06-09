
def is_valid_hq_string(s):
    return "HQ" in s and s.count("H") % 2 == 0 and s.count("Q") % 2 == 0

