
def f1(encrypted_password):
    # Initialize variables
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [chr(i) for i in range(97, 123) if chr(i) not in vowels]
    num_ways = 0

    # Iterate through all possible passwords
    for password in itertools.product(vowels, consonants, vowels, consonants):
        # Check if the current password produces the encrypted password
        if "".join(password) == encrypted_password:
            num_ways += 1

    return num_ways % 1000009

def f2(encrypted_password):
    # Initialize variables
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [chr(i) for i in range(97, 123) if chr(i) not in vowels]
    num_ways = 0

    # Iterate through all possible passwords
    for password in itertools.product(vowels, consonants, vowels, consonants):
        # Check if the current password produces the encrypted password
        if "".join(password) == encrypted_password:
            num_ways += 1

    return num_ways % 1000009

if __name__ == '__main__':
    encrypted_password = input()
    print(f1(encrypted_password))
    print(f2(encrypted_password))

