
def get_corrected_string(string):
    corrected_string = ""
    for char in string:
        if char == "<":
            corrected_string = corrected_string[:-1]
        else:
            corrected_string += char
    return corrected_string

def main():
    string = input()
    corrected_string = get_corrected_string(string)
    print(corrected_string)

if __name__ == '__main__':
    main()

