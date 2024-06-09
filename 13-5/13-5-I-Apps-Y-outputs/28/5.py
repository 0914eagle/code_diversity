
def convert_string(s):
    return s.replace(",", " ")

def main():
    s = input("Enter a string: ")
    converted_string = convert_string(s)
    print(converted_string)

if __name__ == '__main__':
    main()

