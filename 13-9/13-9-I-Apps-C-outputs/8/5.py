
def get_binary_representation(n):
    return bin(n)[2:]

def get_signed_binary_representation(n):
    binary_representation = get_binary_representation(n)
    signed_binary_representation = []
    for digit in binary_representation:
        if digit == '0':
            signed_binary_representation.append('0')
        elif digit == '1':
            signed_binary_representation.append('+')
        else:
            signed_binary_representation.append('-')
    return ''.join(signed_binary_representation)

def get_minimal_signed_binary_representation(n):
    binary_representation = get_binary_representation(n)
    minimal_signed_binary_representation = []
    for digit in binary_representation:
        if digit == '0':
            minimal_signed_binary_representation.append('0')
            break
        elif digit == '1':
            minimal_signed_binary_representation.append('+')
        else:
            minimal_signed_binary_representation.append('-')
    return ''.join(minimal_signed_binary_representation)

def main():
    n = int(input())
    print(get_minimal_signed_binary_representation(n))

if __name__ == '__main__':
    main()

