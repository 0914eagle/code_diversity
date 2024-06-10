
def encrypt(s: str) -> str:
    def shift_char(char, shift):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def encrypt_string(input_str):
        return ''.join(shift_char(char, 2 * 2) for char in input_str)

    return encrypt_string(s)

# Test cases
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
