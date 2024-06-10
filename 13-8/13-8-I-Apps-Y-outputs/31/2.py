
def get_original_string(input_string):
    original_string = ""
    for char in input_string:
        if char == "<":
            original_string = original_string[:-1]
        else:
            original_string += char
    return original_string

def main():
    input_string = input()
    original_string = get_original_string(input_string)
    print(original_string)

if __name__ == '__main__':
    main()

