
def is_valid(s):
    if len(s) <= 2:
        return False
    for i in range(1, len(s) - 1):
        if s[i] == s[i-1] or s[i] == s[i+1]:
            return False
    return True

def play_game(s):
    if not is_valid(s):
        return "Second"
    if len(s) == 3:
        return "First"
    s = s[1:-1]
    return play_game(s)

def main():
    s = input()
    print(play_game(s))

if __name__ == '__main__':
    main()

