
def is_odd(n):
    return n % 2 == 1

def play_game(n):
    if n == 1:
        return "Alice"
    elif n == 2:
        return "Bob"
    else:
        if is_odd(n):
            return "Alice"
        else:
            return "Bob"

if __name__ == '__main__':
    n = int(input())
    print(play_game(n))

