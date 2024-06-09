
def get_dog_name(n):
    if n <= 26:
        return chr(96 + n)
    elif n <= 702:
        return chr(96 + (n // 26)) + chr(96 + (n % 26))
    elif n <= 18278:
        return chr(96 + (n // 26)) + chr(96 + (n % 26)) + chr(96 + ((n % 702) // 26))
    elif n <= 475254:
        return chr(96 + (n // 26)) + chr(96 + (n % 26)) + chr(96 + ((n % 702) // 26)) + chr(96 + ((n % 18278) // 26))
    else:
        return chr(96 + (n // 26)) + chr(96 + (n % 26)) + chr(96 + ((n % 702) // 26)) + chr(96 + ((n % 18278) // 26)) + chr(96 + ((n % 475254) // 26))

if __name__ == '__main__':
    n = int(input())
    print(get_dog_name(n))

