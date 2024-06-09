
def is_happy(ticket):
    n = len(ticket) // 2
    return sum(map(int, ticket[:n])) == sum(map(int, ticket[n:]))

def solve(n, ticket):
    if is_happy(ticket):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(solve(n, ticket))

