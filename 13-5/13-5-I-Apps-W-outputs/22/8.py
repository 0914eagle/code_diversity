
def get_common_substring(strings):
    common_substring = ""
    for i in range(len(strings[0])):
        for j in range(len(strings[0]) - i):
            if all(strings[0][i:i+j] in s for s in strings):
                common_substring = strings[0][i:i+j]
                break
        if common_substring:
            break
    return common_substring

def get_original_string(strings):
    common_substring = get_common_substring(strings)
    original_string = ""
    for string in strings:
        original_string += string.replace(common_substring, "")
    return original_string

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    original_string = get_original_string(strings)
    if len(original_string) == n:
        print(original_string)
    else:
        print(-1)

if __name__ == '__main__':
    main()

