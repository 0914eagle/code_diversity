
def bear_and_string(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if "bear" in s[i:j+1]:
                count += 1
    return count

