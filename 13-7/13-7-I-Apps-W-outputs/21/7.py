
def count_bear_substring(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[j-4:j] == "bear":
                count += 1
    return count

