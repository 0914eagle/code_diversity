
def is_beautiful(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


def get_beautiful_string(s):
    for i in range(s.count("?")):
        if s[0] == "?":
            s = "a" + s[1:]
        elif s[-1] == "?":
            s = s[:-1] + "a"
        else:
            s = s[:i] + "a" + s[i + 1 :]
    return s


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        if "?" not in s:
            print(-1)
        else:
            beautiful_string = get_beautiful_string(s)
            if is_beautiful(beautiful_string):
                print(beautiful_string)
            else:
                print(-1)


if __name__ == "__main__":
    main()

