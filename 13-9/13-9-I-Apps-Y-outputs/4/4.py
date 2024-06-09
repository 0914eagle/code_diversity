
def check_password(stored_password, entered_password):
    if stored_password == entered_password:
        return "Yes"
    elif entered_password[1:] == stored_password:
        return "Yes"
    elif entered_password[:-1] == stored_password:
        return "Yes"
    elif entered_password.lower() == stored_password:
        return "Yes"
    else:
        return "No"

