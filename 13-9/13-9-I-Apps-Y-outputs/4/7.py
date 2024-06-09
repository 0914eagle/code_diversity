
def check_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return "Yes"
    if attempted_password.startswith(stored_password):
        return "Yes"
    if attempted_password.endswith(stored_password):
        return "Yes"
    if attempted_password.lower() == stored_password:
        return "Yes"
    return "No"

