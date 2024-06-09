
def convert_to_space_separated_string(s):
    return s.replace(",", " ")

def main():
    s = input("Enter a string with commas: ")
    print(convert_to_space_separated_string(s))

if __name__ == '__main__':
    main()

