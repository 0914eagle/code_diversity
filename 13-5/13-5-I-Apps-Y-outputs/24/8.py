
def is_even(n):
    return n % 2 == 0

def get_winner(n):
    if is_even(n):
        return "Bob"
    else:
        return "Alice"

if __name__ == '__main__':
    n = int(input())
    print(get_winner(n))

