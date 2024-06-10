
def get_longest_acgt_substring(s):
    longest_acgt_substring = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_acgt_substring(substring):
                longest_acgt_substring = max(longest_acgt_substring, substring, key=len)
    return len(longest_acgt_substring)

def is_acgt_substring(s):
    return all(c in ["A", "C", "G", "T"] for c in s)

if __name__ == '__main__':
    s = input()
    print(get_longest_acgt_substring(s))

