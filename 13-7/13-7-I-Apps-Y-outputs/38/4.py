
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
        delete_index = []
        for i in range(1, len(s), 2):
            if s[i] == s[i-1]:
                delete_index.append(i)
        for i in sorted(delete_index, reverse=True):
            s = s[:i] + s[i+1:]
        return s

def main():
    n = int(input())
    s = input()
    k = len(s) - len(delete_characters(s))
    print(k)
    print(delete_characters(s))

if __name__ == '__main__':
    main()

