
def check_password(s, p):
    if s == p:
        return "Yes"
    if p.startswith(s):
        return "Yes"
    if p.endswith(s):
        return "Yes"
    if p.lower() == s.lower():
        return "Yes"
    return "No"

