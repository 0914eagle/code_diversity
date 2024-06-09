
def is_valid_message(password, message):
    password_chars = set(password)
    for i, char in enumerate(message):
        if char in password_chars:
            password_chars.remove(char)
            if not password_chars:
                return "PASS"
        else:
            return "FAIL"
    return "FAIL"

