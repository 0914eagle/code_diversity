
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return "NO"
    
    sums = [0] * n
    for i in range(n):
        sums[i] = sums[i-1] + int(ticket[i])
    
    for i in range(n):
        for j in range(i+1, n):
            if sums[j] - sums[i] == sums[n-1] - sums[j-1]:
                return "YES"
    
    return "NO"

def main():
    n = int(input())
    ticket = input()
    print(is_lucky_ticket(ticket))

if __name__ == '__main__':
    main()

