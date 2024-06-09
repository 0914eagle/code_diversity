
def f1(n, a, e):
    # Calculate the number of battles Atli can win
    battles = 0
    for i in range(n):
        if a >= e[i]:
            battles += 1
            a -= e[i]
    return battles

def f2(n, a, e):
    # Sort the list of ships sent by Finni in descending order
    e.sort(reverse=True)
    # Calculate the number of battles Atli can win
    battles = 0
    for i in range(n):
        if a >= e[i]:
            battles += 1
            a -= e[i]
    return battles

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    e = list(map(int, input().split()))
    print(f2(n, a, e))

