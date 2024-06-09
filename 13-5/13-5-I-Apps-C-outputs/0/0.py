
def get_original_passwords(encrypted_password):
    original_passwords = []
    for i in range(len(encrypted_password)):
        if encrypted_password[i].islower():
            original_passwords.append(encrypted_password[i])
        elif encrypted_password[i].isupper():
            original_passwords.append(encrypted_password[i].lower())
        else:
            original_passwords.append(encrypted_password[i])
    
    return original_passwords

def get_number_of_ways(original_passwords):
    number_of_ways = 1
    for i in range(len(original_passwords)):
        if original_passwords[i].islower():
            number_of_ways *= 2
        elif original_passwords[i].isupper():
            number_of_ways *= 2
        else:
            number_of_ways *= 1
    
    return number_of_ways

def main():
    encrypted_password = input()
    original_passwords = get_original_passwords(encrypted_password)
    number_of_ways = get_number_of_ways(original_passwords)
    print(number_of_ways % 1000009)

if __name__ == '__main__':
    main()

