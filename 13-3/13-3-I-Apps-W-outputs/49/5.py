
def is_bracket_sequence(strings):
    stack = []
    for string in strings:
        for char in string:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    return False
    return not stack

def main():
    num_strings = int(input())
    strings = [input() for _ in range(num_strings)]
    print("Yes") if is_bracket_sequence(strings) else print("No")

if __name__ == '__main__':
    main()

