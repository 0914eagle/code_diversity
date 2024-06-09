
def get_largest_number(numbers):
    return max(numbers)

def get_base_and_xor_language(largest_number):
    base = 1
    xor_language = ""
    while largest_number > 0:
        remainder = largest_number % base
        if remainder == 0:
            xor_language += "ABRACADABRA"
        largest_number //= base
        base += 1
    return xor_language

def get_string_from_xor_language(xor_language):
    string = ""
    for char in xor_language:
        if char == "A":
            string += "1"
        elif char == "B":
            string += "0"
        elif char == "R":
            string += "1"
        elif char == "C":
            string += "0"
        elif char == "D":
            string += "1"
        elif char == "A":
            string += "0"
        elif char == "B":
            string += "1"
        elif char == "R":
            string += "0"
        elif char == "A":
            string += "1"
    return string

def get_output(numbers):
    largest_number = get_largest_number(numbers)
    xor_language = get_base_and_xor_language(largest_number)
    string = get_string_from_xor_language(xor_language)
    return string

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_output(numbers))

