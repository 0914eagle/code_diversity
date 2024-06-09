
def is_sorted(s, k):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] > s[j] and abs(i-j) < k:
                return "No"
    return "Yes"

