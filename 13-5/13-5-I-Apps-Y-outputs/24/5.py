
def is_odd(n):
    return n % 2 == 1

def play_game(n):
    if n == 1:
        return "Alice"
    if n == 2:
        return "Bob"
    if is_odd(n):
        return play_game(n - 1)
    else:
        return play_game(n - 2)

if __name__ == '__main__':
    n = int(input())
    print(play_game(n))

