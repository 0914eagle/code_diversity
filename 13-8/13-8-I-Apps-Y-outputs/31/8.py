
def clean_string(input_string):
    output_string = ""
    for char in input_string:
        if char == "<":
            output_string = output_string[:-1]
        else:
            output_string += char
    return output_string

def main():
    input_string = input()
    output_string = clean_string(input_string)
    print(output_string)

if __name__ == '__main__':
    main()

