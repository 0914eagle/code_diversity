
def f1(n, m, pegs):
    # Initialize a list to store the pegs
    pegs = [0] * (n + 1)
    
    # Iterate through the pegs and update the list
    for i in range(m):
        pegs[pegs[i]] += 1
    
    # Return the number of pegs used
    return sum(pegs)

def f2(n, m, pegs):
    # Initialize a list to store the pegs
    pegs = [0] * (n + 1)
    
    # Iterate through the pegs and update the list
    for i in range(m):
        pegs[pegs[i]] += 1
    
    # Return the number of pegs used
    return sum(pegs)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    pegs = list(map(int, input().split()))
    print(f1(n, m, pegs))
    print(f2(n, m, pegs))

