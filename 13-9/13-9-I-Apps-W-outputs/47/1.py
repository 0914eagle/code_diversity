
def get_original_string(code_string):
    original_string = ""
    for i in range(len(code_string)):
        if code_string[i].isdigit():
            repeat_count = int(code_string[i])
            j = i + 1
            while j < len(code_string) and code_string[j] != "-":
                original_string += code_string[j]
                j += 1
            i = j
        else:
            original_string += code_string[i]
    return original_string

def is_palindrome(string):
    return string == string[::-1]

def solve(code_string):
    original_string = get_original_string(code_string)
    if is_palindrome(original_string):
        return "Return"
    else:
        return "Continue"

if __name__ == '__main__':
    code_string = input()
    print(solve(code_string))

