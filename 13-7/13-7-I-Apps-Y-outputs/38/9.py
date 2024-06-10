
def is_good_string(s):
    if len(s) % 2 == 0:
        return True
    else:
        for i in range(1, len(s), 2):
            if s[i] == s[i - 1]:
                return False
        return True

def delete_characters(s):
    if len(s) == 0:
        return s
    else:
        if is_good_string(s):
            return s
        else:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == s[i - 1]:
                    return s[:i]
            return s

def main():
    n = int(input())
    s = input()
    k = len(s) - len(delete_characters(s))
    print(k)
    print(delete_characters(s))

if __name__ == '__main__':
    main()

