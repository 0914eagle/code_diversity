
def is_periodic(s, k):
    if len(s) % k != 0:
        return False
    
    sub_strings = [s[i:i+k] for i in range(0, len(s), k)]
    for i in range(1, len(sub_strings)):
        if sub_strings[i] != sub_strings[i-1][1:] + sub_strings[i-1][0]:
            return False
    return True

def get_period(s):
    for k in range(1, len(s)):
        if is_periodic(s, k):
            return k
    return 0

if __name__ == '__main__':
    s = input()
    print(get_period(s))

