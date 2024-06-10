
def is_good_string(s):
    if len(s) % 2 == 0:
        return True
    else:
        for i in range(1, len(s), 2):
            if s[i] == s[i-1]:
                return False
        return True

def delete_characters(s):
    if is_good_string(s):
        return s
    else:
        for i in range(len(s)-1, -1, -1):
            if s[i] == s[i-1]:
                return s[:i]
        return ""

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(len(s) - delete_characters(s))
    print(delete_characters(s))

