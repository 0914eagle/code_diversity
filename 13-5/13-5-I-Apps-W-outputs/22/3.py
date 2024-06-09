
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

def get_swapped_strings(common_substring, strings):
    swapped_strings = []
    for string in strings:
        swapped_strings.append(common_substring + string[len(common_substring):])
    return swapped_strings

def f1(k, n):
    strings = []
    for _ in range(k):
        strings.append(input())
    common_substring = get_common_substring(strings)
    if not common_substring:
        return "-1"
    swapped_strings = get_swapped_strings(common_substring, strings)
    if swapped_strings == strings:
        return common_substring
    else:
        return "-1"

def f2(k, n):
    strings = []
    for _ in range(k):
        strings.append(input())
    common_substring = get_common_substring(strings)
    if not common_substring:
        return "-1"
    swapped_strings = get_swapped_strings(common_substring, strings)
    if swapped_strings == strings:
        return common_substring
    else:
        return "-1"

if __name__ == '__main__':
    k, n = map(int, input().split())
    print(f1(k, n))
    print(f2(k, n))

