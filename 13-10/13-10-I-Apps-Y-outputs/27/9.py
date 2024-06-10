
def check_duplicates(my_string):
    return len(set(my_string)) == len(my_string)

def check_exact_two_kinds(my_string):
    unique_chars = set(my_string)
    return len(unique_chars) == 2 and all(my_string.count(char) == 2 for char in unique_chars)

def main():
    my_string = input("Enter a 4-character string: ")
    if check_duplicates(my_string) and check_exact_two_kinds(my_string):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

