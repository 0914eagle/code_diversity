
def find_first_return_day(n, p):
    # Initialize a list to store the number of days each kid has owned their book
    days_owned = [0] * n
    
    # Loop through each day
    for day in range(1, n + 1):
        # Loop through each kid and find the new owner of their book
        for i in range(n):
            owner = p[i]
            days_owned[owner - 1] += 1
        
        # Check if any kid has returned their book to themselves
        for i in range(n):
            if days_owned[i] == 1:
                return day
    
    # If no kid has returned their book, return -1
    return -1

def main():
    queries = int(input())
    
    for query in range(queries):
        n = int(input())
        p = list(map(int, input().split()))
        print(*find_first_return_day(n, p))

if __name__ == '__main__':
    main()

