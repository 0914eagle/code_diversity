
def get_dog_name(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    while n > 0:
        n, remainder = divmod(n-1, 26)
        name = alphabet[remainder] + name
    return name

