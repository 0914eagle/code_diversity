
def is_valid_string(s):
    if len(s) != 4:
        return False
    if not s.isupper():
        return False
    return True

def is_two_kinds_of_characters(s):
    if not is_valid_string(s):
        return False
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
    return count == 2

def main():
    s = input("Enter a 4-character string: ")
    if is_two_kinds_of_characters(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

