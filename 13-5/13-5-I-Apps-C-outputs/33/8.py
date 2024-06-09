
def check_string(s):
    a_count = s.count('a')
    b_count = s.count('b')
    c_count = s.count('c')
    if a_count + b_count == c_count or a_count + c_count == b_count or b_count + c_count == a_count:
        return "YES"
    else:
        return "NO"

