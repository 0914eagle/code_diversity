
def is_equivalent(s1, s2):
    if s1 == s2:
        return "YES"
    if len(s1) % 2 == 1:
        return "NO"
    mid = len(s1) // 2
    s1_1, s1_2 = s1[:mid], s1[mid:]
    s2_1, s2_2 = s2[:mid], s2[mid:]
    if s1_1 == s2_2 and s1_2 == s2_1:
        return "YES"
    return "NO"

