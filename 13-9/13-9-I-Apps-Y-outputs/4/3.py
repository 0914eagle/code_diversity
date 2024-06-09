
def check_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return "Yes"
    elif stored_password.startswith(attempted_password):
        return "Yes"
    elif stored_password.endswith(attempted_password):
        return "Yes"
    elif stored_password.lower() == attempted_password.lower():
        return "Yes"
    else:
        return "No"

