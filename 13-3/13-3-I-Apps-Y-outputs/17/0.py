
def get_dog_name(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    names = []
    while n > 0:
        names.append(alphabet[n % 26])
        n //= 26
    return "".join(reversed(names))

