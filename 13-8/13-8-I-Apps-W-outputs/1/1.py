
def check_sequence(a, b):
    # Initialize a dictionary to store the elements of b
    b_dict = {}
    for i in range(len(b)):
        b_dict[b[i]] = 1
    
    # Initialize a flag to indicate if the sequence is increasing
    increasing = True
    
    # Iterate through the elements of a
    for i in range(len(a)):
        # If the element is zero, check if there are any elements left in b
        if a[i] == 0:
            if len(b_dict) == 0:
                return False
            # Get the first element from b and remove it from the dictionary
            element = list(b_dict.keys())[0]
            b_dict.pop(element)
            a[i] = element
        # If the element is not zero, check if it is increasing
        elif a[i] < a[i-1] and increasing:
            increasing = False
    
    # If the sequence is increasing, return False
    if increasing:
        return False
    
    # If the sequence is not increasing, return True
    return True

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes") if check_sequence(a, b) else print("No")

if __name__ == '__main__':
    main()

