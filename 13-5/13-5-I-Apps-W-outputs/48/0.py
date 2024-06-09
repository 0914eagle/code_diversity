
def is_lucky(ticket):
    n = len(ticket)
    if n == 1:
        return "YES"
    if n == 2:
        return "NO"
    for i in range(1, n):
        if ticket[:i] == ticket[n-i:]:
            return "YES"
    return "NO"

def solve():
    n = int(input())
    ticket = input()
    print(is_lucky(ticket))

if __name__ == '__main__':
    solve()

