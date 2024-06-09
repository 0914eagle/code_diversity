
def validate_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return "Yes"
    elif attempted_password[1:] == stored_password:
        return "Yes"
    elif attempted_password[:-1] == stored_password:
        return "Yes"
    elif attempted_password.lower() == stored_password.lower():
        return "Yes"
    else:
        return "No"

