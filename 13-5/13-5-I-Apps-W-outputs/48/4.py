
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    # convert the ticket to a list of integers
    ticket = [int(x) for x in ticket]
    
    # sum of the digits in the ticket
    total = sum(ticket)
    
    # find all possible segments
    segments = []
    for i in range(1, n):
        for j in range(i, n):
            segments.append(ticket[i:j+1])
    
    # check if any two segments have the same sum
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if sum(segments[i]) == sum(segments[j]):
                return "YES"
    
    return "NO"

def main():
    n = int(input())
    ticket = input()
    print(is_lucky_ticket(ticket))

if __name__ == '__main__':
    main()

