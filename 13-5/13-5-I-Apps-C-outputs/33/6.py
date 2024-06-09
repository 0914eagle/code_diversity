
def check_string(s):
    a_count = s.count('a')
    b_count = s.count('b')
    c_count = s.count('c')
    if a_count == 0 or b_count == 0:
        return "NO"
    if c_count == a_count or c_count == b_count:
        return "YES"
    return "NO"

