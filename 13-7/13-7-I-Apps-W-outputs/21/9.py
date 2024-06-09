
def bear_and_string(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if "bear" in s[i:j]:
                count += 1
    return count

