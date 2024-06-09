
def solve(encrypted_password):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for i in range(len(encrypted_password)):
        if encrypted_password[i] in vowels:
            continue
        else:
            count += 1
    return count

