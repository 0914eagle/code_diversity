
def f1(N1, N2, row1, row2, T):
    # Initialize the order of the ants after T seconds
    order = []
    
    # Loop through each second
    for i in range(T):
        # Loop through each ant in the first row
        for j in range(N1):
            # If the ant is not the first ant in the first row
            if j > 0:
                # Get the position of the ant in the second row that is behind the current ant in the first row
                pos = N2 - j
                # If the ant in the second row is moving in the opposite direction
                if row2[pos] < row1[j]:
                    # Swap the positions of the two ants
                    row1[j], row2[pos] = row2[pos], row1[j]
    
    # Add the ants in the first row to the order
    order += row1
    # Add the ants in the second row to the order
    order += row2
    
    return "".join(order)

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    N1 = int(input())
    N2 = int(input())
    row1 = input()
    row2 = input()
    T = int(input())
    
    print(f1(N1, N2, row1, row2, T))

