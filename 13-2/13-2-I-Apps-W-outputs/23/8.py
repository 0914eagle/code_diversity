
def get_unique_substrings(strings, substring):
    unique_substrings = set()
    for string in strings:
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                sub = string[i:j]
                if sub == substring:
                    unique_substrings.add(sub)
    return len(unique_substrings)

def main():
    num_strings = int(input())
    strings = []
    for i in range(num_strings):
        strings.append(input())
    substring_len = int(input())
    substring = input()
    print(get_unique_substrings(strings, substring))

if __name__ == '__main__':
    main()

