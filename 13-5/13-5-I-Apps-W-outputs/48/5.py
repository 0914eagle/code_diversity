
def is_lucky_ticket(ticket):
    n = len(ticket)
    if n < 2:
        return False
    
    sum1 = 0
    for i in range(n//2):
        sum1 += int(ticket[i])
    
    sum2 = 0
    for i in range(n//2, n):
        sum2 += int(ticket[i])
    
    return sum1 == sum2

def main():
    n = int(input())
    ticket = input()
    if is_lucky_ticket(ticket):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

