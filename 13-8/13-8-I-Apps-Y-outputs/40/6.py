
def is_periodic(s, k):
    if len(s) % k != 0:
        return False
    
    substring_length = len(s) // k
    substrings = [s[i:i + substring_length] for i in range(0, len(s), substring_length)]
    
    for i in range(1, len(substrings)):
        if substrings[i] != substrings[i - 1][1:] + substrings[i - 1][0]:
            return False
    
    return True

def find_smallest_period(s):
    for k in range(1, len(s)):
        if is_periodic(s, k):
            return k
    
    return len(s)

if __name__ == '__main__':
    s = input()
    print(find_smallest_period(s))

