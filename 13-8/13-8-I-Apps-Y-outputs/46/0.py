
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def play_game(n, a):
    alice = 0
    bob = 0
    while n > 0:
        if n % 2 == 0:
            alice += a[n-1]
            bob += a[n-2]
        else:
            alice += a[n-2]
            bob += a[n-1]
        n -= 1
    return alice, bob

def main():
    n, a = get_input()
    alice, bob = play_game(n, a)
    print(alice, bob)

if __name__ == '__main__':
    main()

