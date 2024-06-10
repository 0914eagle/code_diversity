
def is_valid_move(s):
    if len(s) <= 2:
        return False
    if s[0] == s[1] or s[-1] == s[-2]:
        return False
    return True

def takahashi_wins(s):
    if not is_valid_move(s):
        return False
    return takahashi_wins(s[1:-1])

def aoki_wins(s):
    if not is_valid_move(s):
        return True
    return aoki_wins(s[1:-1])

def main():
    s = input()
    if takahashi_wins(s):
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    main()

