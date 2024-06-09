
def get_dog_name(n):
    if n <= 26:
        return chr(96 + n)
    elif n <= 702:
        return chr(96 + (n - 1) % 26) + chr(96 + (n - 1) // 26)
    elif n <= 18278:
        return chr(96 + (n - 1) % 26) + chr(96 + ((n - 1) // 26) % 26) + chr(96 + (n - 1) // 676)
    else:
        return chr(96 + (n - 1) % 26) + chr(96 + ((n - 1) // 26) % 26) + chr(96 + ((n - 1) // 676) % 26) + chr(96 + (n - 1) // 17576)

if __name__ == '__main__':
    n = int(input())
    print(get_dog_name(n))

