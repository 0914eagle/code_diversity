
def get_candy_sizes(n):
    return list(map(int, input().split()))

def get_move_count(n, a):
    alice_moves = 0
    bob_moves = 0
    total_alice_moves = 0
    total_bob_moves = 0
    while n > 0:
        if alice_moves == 0:
            alice_moves = 1
            bob_moves = 0
        elif bob_moves == 0:
            bob_moves = 1
            alice_moves = 0
        else:
            if alice_moves < bob_moves:
                alice_moves += 1
            elif bob_moves < alice_moves:
                bob_moves += 1
            else:
                alice_moves += 1
                bob_moves += 1
        total_alice_moves += alice_moves
        total_bob_moves += bob_moves
        n -= alice_moves + bob_moves
    return total_alice_moves, total_bob_moves

def get_alice_and_bobs_candy_sizes(n, a):
    alice_sizes = []
    bob_sizes = []
    for i in range(n):
        if i % 2 == 0:
            alice_sizes.append(a[i])
        else:
            bob_sizes.append(a[i])
    return alice_sizes, bob_sizes

def get_total_candy_sizes(alice_sizes, bob_sizes):
    return sum(alice_sizes), sum(bob_sizes)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = get_candy_sizes(n)
        alice_sizes, bob_sizes = get_alice_and_bobs_candy_sizes(n, a)
        alice_moves, bob_moves = get_move_count(n, a)
        alice_total, bob_total = get_total_candy_sizes(alice_sizes, bob_sizes)
        print(alice_moves, alice_total, bob_total)

if __name__ == '__main__':
    main()

