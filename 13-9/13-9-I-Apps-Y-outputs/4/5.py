
def is_valid_password(stored_password, entered_password):
    # Check if the stored and entered passwords are identical
    if stored_password == entered_password:
        return True

    # Check if the entered password can be formed by prepending a single digit to the stored password
    if entered_password[1:] == stored_password:
        return True

    # Check if the entered password can be formed by appending a single digit to the stored password
    if stored_password[1:] == entered_password:
        return True

    # Check if the entered password is equal to the stored password after reversing the case of all letters
    if stored_password.lower() == entered_password.lower():
        return True

    # If none of the above conditions are met, return False
    return False

