
def is_duplicate_pair(s):
    if len(s) != 4:
        return "No"
    count = 0
    for i in range(1, len(s)):
        if s[0] == s[i]:
            count += 1
    if count == 2:
        return "Yes"
    else:
        return "No"

def main():
    s = input()
    print(is_duplicate_pair(s))

if __name__ == '__main__':
    main()

