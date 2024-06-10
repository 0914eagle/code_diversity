
def get_available_letters(s, c):
    available_letters = []
    for letter in c:
        if letter in s:
            available_letters.append(letter)
    return available_letters

def get_substrings(s, available_letters):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if all(letter in available_letters for letter in substring):
                substrings.append(substring)
    return substrings

def count_substrings(s, available_letters):
    return len(get_substrings(s, available_letters))

def main():
    n, k = map(int, input().split())
    s = input()
    c = input()
    available_letters = get_available_letters(s, c)
    print(count_substrings(s, available_letters))

if __name__ == '__main__':
    main()

