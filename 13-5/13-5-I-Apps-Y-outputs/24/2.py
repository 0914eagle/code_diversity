
def is_even(n):
    return n % 2 == 0

def find_winner(n):
    if is_even(n):
        return "Bob"
    else:
        return "Alice"

if __name__ == '__main__':
    n = int(input())
    print(find_winner(n))

