
def is_valid_message(password, message):
    password_chars = set(password)
    for i, char in enumerate(message):
        if char in password_chars:
            if char != password[i % len(password)]:
                return "FAIL"
    return "PASS"

