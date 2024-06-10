
def get_charges(n, c, t):
    # Initialize the charges as a list of tuples (c_i, t_i)
    charges = [(ci, ti) for ci, ti in zip(c, t)]
    
    # Iterate through the charges and check if they are equal
    for i in range(n):
        if charges[i][0] != charges[i][1]:
            # If the charges are not equal, return "No"
            return "No"
    
    # If all charges are equal, return "Yes"
    return "Yes"

def main():
    n = int(input())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(get_charges(n, c, t))

if __name__ == '__main__':
    main()

