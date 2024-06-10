
def solve(n, pieces):
    pieces = sorted(pieces, reverse=True)
    alice = []
    bob = []
    for i in range(n):
        if i % 2 == 0:
            alice.append(pieces[i])
        else:
            bob.append(pieces[i])
    return sum(alice), sum(bob)

