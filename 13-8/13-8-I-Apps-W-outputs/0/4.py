
def is_synchronizable(c_charges, t_charges):
    
    if len(c_charges) != len(t_charges):
        return False
    
    # Initialize a queue with the indices of the stones that need to be synchronized
    queue = [i for i in range(1, len(c_charges))]
    
    while queue:
        i = queue.pop(0)
        ci, ti = c_charges[i], t_charges[i]
        if ci != ti:
            # Synchronize the stone with its neighbors
            c_charges[i] = c_charges[i-1] + c_charges[i+1] - ci
            queue.append(i-1)
            queue.append(i+1)
    
    # Check if all the charges are equal to the required ones
    return all(c == t for c, t in zip(c_charges, t_charges))

def main():
    n = int(input())
    c_charges = list(map(int, input().split()))
    t_charges = list(map(int, input().split()))
    
    print("Yes") if is_synchronizable(c_charges, t_charges) else print("No")

if __name__ == '__main__':
    main()

