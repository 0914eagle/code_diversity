
def get_common_string(strings):
    common_string = ""
    for i in range(len(strings[0])):
        count = 0
        for string in strings:
            if string[i] == common_string[i]:
                count += 1
        if count == len(strings):
            common_string += strings[0][i]
    return common_string

def get_swapped_strings(common_string, strings):
    swapped_strings = []
    for string in strings:
        swapped_strings.append("".join(common_string))
    return swapped_strings

def is_valid_string(string):
    for i in range(len(string)):
        if string[i] != string[(i+1)%len(string)]:
            return False
    return True

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    common_string = get_common_string(strings)
    swapped_strings = get_swapped_strings(common_string, strings)
    if is_valid_string(common_string):
        print(common_string)
    else:
        print(-1)

if __name__ == '__main__':
    main()

