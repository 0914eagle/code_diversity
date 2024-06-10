
def get_longest_acgt_substring(s):
    longest_substring = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if is_acgt_string(substring):
                if len(substring) > len(longest_substring):
                    longest_substring = substring
    return len(longest_substring)

def is_acgt_string(s):
    for c in s:
        if c not in "ACGT":
            return False
    return True

if __name__ == '__main__':
    s = input()
    print(get_longest_acgt_substring(s))

