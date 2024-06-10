
def remove_special_characters(string):
    return ''.join([char for char in string if char not in '<>'])

def solve(string):
    string = remove_special_characters(string)
    stack = []
    for char in string:
        if char == '<':
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

if __name__ == '__main__':
    string = input()
    print(solve(string))

