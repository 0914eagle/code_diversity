
def get_alice_sum(n, pieces):
    pieces.sort()
    return sum(pieces[:n//2])

def get_bob_sum(n, pieces):
    pieces.sort()
    return sum(pieces[n//2:])

def main():
    n = int(input())
    pieces = list(map(int, input().split()))
    alice_sum = get_alice_sum(n, pieces)
    bob_sum = get_bob_sum(n, pieces)
    print(alice_sum, bob_sum)

if __name__ == '__main__':
    main()

