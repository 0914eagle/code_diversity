
def convert_to_space_separated_string(s):
    return s.replace(",", " ")

def main():
    s = input("Enter a string with commas: ")
    converted_string = convert_to_space_separated_string(s)
    print(converted_string)

if __name__ == '__main__':
    main()

