
def find_longest_subsequence(s, t):
    # Find the longest common substring
    # between s and t
    longest_common_substring = ""
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                curr_substring = s[i]
                k = 1
                while i + k < len(s) and j + k < len(t) and s[i + k] == t[j + k]:
                    curr_substring += s[i + k]
                    k += 1
                if len(longest_common_substring) < len(curr_substring):
                    longest_common_substring = curr_substring
    return len(s) - len(longest_common_substring)

def main():
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    print(find_longest_subsequence(s, t))

if __name__ == '__main__':
    main()

