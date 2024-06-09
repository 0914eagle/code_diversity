
def get_largest_element(numbers):
    return max(numbers)

def get_base_and_xor_language(largest_element):
    if largest_element == 1:
        return "Binary"
    elif largest_element == 2:
        return "Octal"
    elif largest_element == 3:
        return "Hexadecimal"
    else:
        return "Unknown"

def get_string(base_and_xor_language):
    if base_and_xor_language == "Binary":
        return "01"
    elif base_and_xor_language == "Octal":
        return "01234567"
    elif base_and_xor_language == "Hexadecimal":
        return "0123456789ABCDEF"
    else:
        return "Unknown"

def get_distorted_mathematics(string):
    return string[::-1]

def get_magic_word(string):
    return "".join(reversed(string))

def get_stack_rupture(magic_word):
    return magic_word.upper()

def get_output(stack_rupture):
    return len(stack_rupture)

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    largest_element = get_largest_element(numbers)
    base_and_xor_language = get_base_and_xor_language(largest_element)
    string = get_string(base_and_xor_language)
    distorted_mathematics = get_distorted_mathematics(string)
    magic_word = get_magic_word(string)
    stack_rupture = get_stack_rupture(magic_word)
    output = get_output(stack_rupture)
    print(output)

