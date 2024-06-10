
def get_input():
    n = int(input())
    pieces = list(map(int, input().split()))
    return n, pieces

def play_game(n, pieces):
    alice_pieces = []
    bob_pieces = []
    while pieces:
        if n % 2 == 0:
            alice_pieces.append(pieces.pop())
        else:
            bob_pieces.append(pieces.pop())
        n -= 1
    return sum(alice_pieces), sum(bob_pieces)

def main():
    n, pieces = get_input()
    alice_sum, bob_sum = play_game(n, pieces)
    print(alice_sum, bob_sum)

if __name__ == '__main__':
    main()

