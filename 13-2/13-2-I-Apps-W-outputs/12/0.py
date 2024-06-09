
def longest_non_palindrome(s):
    # Find the longest substring that is not a palindrome
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                break
        else:
            longest = max(longest, j - i + 1)
    return longest

