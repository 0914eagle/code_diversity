
def verify_claim(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return "no"
    for i in range(len(s1)):
        if s[i] != s1[i]:
            return "no"
    for i in range(len(s2)):
        if s[i + len(s1)] != s2[i]:
            return "no"
    return "yes"

