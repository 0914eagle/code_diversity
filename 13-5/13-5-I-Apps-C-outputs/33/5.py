
def check_string(s):
    # Check if the string contains at least one 'a' and one 'b'
    if 'a' in s and 'b' in s:
        # Count the number of 'a' and 'b' in the string
        count_a = s.count('a')
        count_b = s.count('b')
        # Check if the number of 'c' is equal to the number of 'a' or 'b'
        if count_a == s.count('c') or count_b == s.count('c'):
            return "YES"
    return "NO"

