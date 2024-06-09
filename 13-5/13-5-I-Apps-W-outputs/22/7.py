
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

def get_restored_string(common_string, strings):
    restored_string = ""
    for i in range(len(common_string)):
        for string in strings:
            if string[i] != common_string[i]:
                restored_string += string[i]
                break
    return restored_string

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    common_string = get_common_string(strings)
    restored_string = get_restored_string(common_string, strings)
    if restored_string:
        print(restored_string)
    else:
        print(-1)

if __name__ == '__main__':
    main()

