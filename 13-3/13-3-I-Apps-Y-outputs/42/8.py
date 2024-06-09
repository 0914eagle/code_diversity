
def convert_to_octal(binary_numeral):
    # Pad the binary numeral with zeros on the left until the number of digits is divisible by 3
    binary_numeral = binary_numeral.zfill(len(binary_numeral) // 3 * 3)

    # Group adjacent binary digits into groups of 3 digits
    groups = [binary_numeral[i:i+3] for i in range(0, len(binary_numeral), 3)]

    # Replace each group of binary digits with the corresponding octal digit
    octal_numeral = ""
    for group in groups:
        if group == "000":
            octal_numeral += "0"
        elif group == "001":
            octal_numeral += "1"
        elif group == "010":
            octal_numeral += "2"
        elif group == "011":
            octal_numeral += "3"
        elif group == "100":
            octal_numeral += "4"
        elif group == "101":
            octal_numeral += "5"
        elif group == "110":
            octal_numeral += "6"
        elif group == "111":
            octal_numeral += "7"

    return octal_numeral

if __name__ == '__main__':
    binary_numeral = input("Enter a binary numeral: ")
    print(convert_to_octal(binary_numeral))

