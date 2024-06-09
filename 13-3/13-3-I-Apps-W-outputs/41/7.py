
def is_sorted(s, k):
    for i in range(len(s)):
        for j in range(i+1, min(len(s), i+k+1)):
            if s[i] > s[j]:
                return "No"
    return "Yes"

