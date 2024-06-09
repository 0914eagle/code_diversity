
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sums = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += int(ticket[j])
            sums.append(sum)
    
    for i in range(n):
        for j in range(i+1, n):
            if sums[i] == sums[j]:
                return "YES"
    
    return "NO"

def main():
    n = int(input())
    ticket = input()
    print(is_lucky_ticket(ticket))

if __name__ == '__main__':
    main()

