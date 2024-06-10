
def is_good_string(s):
    count_zeros = 0
    count_ones = 0
    for c in s:
        if c == '0':
            count_zeros += 1
        else:
            count_ones += 1
    return count_zeros != count_ones

def find_good_substrings(s):
    if not is_good_string(s):
        return []
    substrings = []
    current_substring = ''
    for i in range(len(s)):
        current_substring += s[i]
        if not is_good_string(current_substring):
            substrings.append(current_substring)
            current_substring = ''
    if current_substring:
        substrings.append(current_substring)
    return substrings

def main():
    n = int(input())
    s = input()
    substrings = find_good_substrings(s)
    print(len(substrings))
    for substring in substrings:
        print(substring, end=' ')

if __name__ == '__main__':
    main()

