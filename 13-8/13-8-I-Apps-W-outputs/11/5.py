
def get_happy_ticket(ticket, n):
    # Initialize variables
    happy_ticket = ""
    erased_digits = []
    
    # Find erased digits
    for i in range(n):
        if ticket[i] == "?":
            erased_digits.append(i)
    
    # Replace erased digits with digits from 0 to 9
    for i in range(len(erased_digits)):
        happy_ticket += str(i)
    
    # Check if the ticket is happy
    if happy_ticket[:n//2] == happy_ticket[n//2:]:
        return True
    else:
        return False

def get_winner(ticket, n):
    # Check if the ticket is happy
    if get_happy_ticket(ticket, n):
        return "Bicarp"
    else:
        return "Monocarp"

if __name__ == '__main__':
    n = int(input())
    ticket = input()
    print(get_winner(ticket, n))

