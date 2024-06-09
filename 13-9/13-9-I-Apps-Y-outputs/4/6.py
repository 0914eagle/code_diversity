
def is_valid_password(stored_password, attempted_password):
    # Check if the stored and attempted passwords are identical
    if stored_password == attempted_password:
        return True

    # Check if the stored password can be formed by prepending a single digit to the attempted password
    if attempted_password.startswith(stored_password):
        return True

    # Check if the stored password can be formed by appending a single digit to the attempted password
    if stored_password in attempted_password:
        return True

    # Check if the stored password is equal to the attempted password after reversing the case of all letters
    if stored_password.lower() == attempted_password.lower():
        return True

    # If none of the above conditions are met, return False
    return False

