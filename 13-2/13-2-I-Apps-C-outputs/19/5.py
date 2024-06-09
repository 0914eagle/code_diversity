
def f1(n, m, pegs):
    # Initialize a list to store the pegs
    pegs_list = []
    
    # Iterate through the pegs and add them to the list
    for i in range(n):
        pegs_list.append(pegs[i])
    
    # Return the list of pegs
    return pegs_list

def f2(n, m, pegs):
    # Initialize a list to store the pegs
    pegs_list = []
    
    # Iterate through the pegs and add them to the list
    for i in range(n):
        pegs_list.append(pegs[i])
    
    # Return the list of pegs
    return pegs_list

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    pegs = [int(x) for x in input().split()]
    print(f1(n, m, pegs))
    print(f2(n, m, pegs))

