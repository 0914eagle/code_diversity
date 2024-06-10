
def is_valid_move(s):
    if len(s) == 1:
        return False
    if s[0] == s[1] or s[-1] == s[-2]:
        return False
    return True

def play_game(s):
    if not is_valid_move(s):
        return "First"
    return "Second"

if __name__ == '__main__':
    s = input()
    print(play_game(s))

