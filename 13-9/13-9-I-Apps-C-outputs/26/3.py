
def find_possible_passwords(encrypted_password):
    possible_passwords = 0
    for i in range(len(encrypted_password)):
        if encrypted_password[i].isalpha():
            possible_passwords += 1
    return possible_passwords

