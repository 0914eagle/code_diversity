
def check_string(s):
    if len(s) != 4:
        return "No"
    if not s.isupper():
        return "No"
    if len(set(s)) != 2:
        return "No"
    return "Yes"

def main():
    s = input("Enter a 4-character string: ")
    print(check_string(s))

if __name__ == '__main__':
    main()

