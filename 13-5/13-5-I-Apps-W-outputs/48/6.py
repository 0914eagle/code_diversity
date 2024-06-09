
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    # convert the ticket to a list of integers
    ticket = [int(x) for x in ticket]
    
    # find the sum of each segment
    sums = []
    for i in range(n):
        for j in range(i+1, n):
            sums.append(sum(ticket[i:j+1]))
    
    # check if there are any equal sums
    for i in range(len(sums)):
        for j in range(i+1, len(sums)):
            if sums[i] == sums[j]:
                return "YES"
    
    return "NO"

def main():
    n = int(input())
    ticket = input()
    print(is_lucky_ticket(ticket))

if __name__ == '__main__':
    main()

