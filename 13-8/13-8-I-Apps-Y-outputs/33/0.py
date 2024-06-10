
def find_longest_acgt_substring(s):
    longest_substring = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if is_acgt_substring(substring):
                longest_substring = max(longest_substring, substring, key=len)
    return len(longest_substring)

def is_acgt_substring(s):
    return all(c in "ACGT" for c in s)

if __name__ == '__main__':
    s = input()
    print(find_longest_acgt_substring(s))

