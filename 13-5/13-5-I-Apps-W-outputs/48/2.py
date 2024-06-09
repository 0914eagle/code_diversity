
def is_lucky(ticket):
    n = len(ticket)
    for i in range(n):
        for j in range(i+1, n):
            if sum(ticket[i:j]) == sum(ticket[j:n]):
                return True
    return False

def main():
    n = int(input())
    ticket = list(map(int, input()))
    if is_lucky(ticket):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

