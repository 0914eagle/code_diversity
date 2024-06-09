
def convert_binary_to_octal(binary_numeral):
    # Pad the binary numeral with zeros on the left until the number of digits is divisible by 3
    binary_numeral = binary_numeral.zfill(len(binary_numeral) // 3 * 3)

    # Group adjacent binary digits into groups of 3 digits
    groups = [binary_numeral[i:i+3] for i in range(0, len(binary_numeral), 3)]

    # Replace each group of binary digits with the corresponding octal digit
    octal_numeral = ""
    for group in groups:
        octal_numeral += str(int(group, 2))

    return octal_numeral

if __name__ == '__main__':
    binary_numeral = input("Enter a binary numeral: ")
    print(convert_binary_to_octal(binary_numeral))

