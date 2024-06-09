
def is_valid_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return True
    
    if attempted_password.startswith(stored_password):
        return True
    
    if stored_password.startswith(attempted_password):
        return True
    
    if attempted_password.lower() == stored_password.lower():
        return True
    
    return False

