
def num_ways(encrypted_password):
    password = ""
    count = 0
    for i in range(len(encrypted_password)):
        if encrypted_password[i].islower():
            password += encrypted_password[i]
        else:
            if encrypted_password[i-1].islower():
                password += encrypted_password[i-1]
            count += 1
    return count

