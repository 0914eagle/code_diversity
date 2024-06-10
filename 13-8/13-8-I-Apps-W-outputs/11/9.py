
def is_happy(ticket):
    n = len(ticket) // 2
    first_half = sum(int(ticket[i]) for i in range(n))
    second_half = sum(int(ticket[i]) for i in range(n, len(ticket)))
    return first_half == second_half

def solve(n, ticket):
    if is_happy(ticket):
        return "Bicarp"
    
    # Find the first erased digit
    for i in range(n):
        if ticket[i] == "?":
            break
    
    # Replace the erased digit with a new one
    ticket = ticket[:i] + str(0) + ticket[i+1:]
    
    # Recursively solve the new ticket
    return solve(n, ticket)

def main():
    n = int(input())
    ticket = input()
    print(solve(n, ticket))

if __name__ == '__main__':
    main()

