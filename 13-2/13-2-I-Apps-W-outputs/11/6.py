
def check_password(password):
    if len(password) < 5:
        return "Too weak"
    if not any(c.isupper() for c in password):
        return "Too weak"
    if not any(c.islower() for c in password):
        return "Too weak"
    if not any(c.isdigit() for c in password):
        return "Too weak"
    return "Correct"

