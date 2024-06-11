def encrypt(s):
    
    # create a list of the alphabet
    alphabet = list(string.ascii_lowercase)
    # create a list of the alphabet rotated by two
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    # create a dictionary of the alphabet and the rotated alphabet
    alphabet_dict = dict(zip(alphabet, rotated_alphabet))
    # create a list of the encrypted string
    encrypted_list = [alphabet_dict[char] for char in s]
    # join the list into a string
    encrypted_string = ''.join(encrypted_list)
    return encrypted_string

print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))

#