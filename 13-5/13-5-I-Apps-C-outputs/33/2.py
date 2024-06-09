
def check_string(s):
    # Check if the string contains at least one 'a' and one 'b'
    if 'a' not in s or 'b' not in s:
        return "NO"
    
    # Count the number of 'a', 'b' and 'c' in the string
    count_a = s.count('a')
    count_b = s.count('b')
    count_c = s.count('c')
    
    # Check if the number of 'c' is equal to the number of 'a' or 'b'
    if count_c == count_a or count_c == count_b:
        return "YES"
    else:
        return "NO"

