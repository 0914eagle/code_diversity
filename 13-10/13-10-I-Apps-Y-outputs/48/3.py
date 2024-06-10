
def get_max_subset(x):
    # Sort the input array
    x.sort()
    
    # Initialize variables
    max_subset = []
    current_subset = []
    previous_element = None
    
    # Iterate through the sorted array
    for element in x:
        # If the current element is a power of two greater than the previous element, add it to the current subset
        if previous_element is not None and element == previous_element * 2:
            current_subset.append(element)
        # If the current element is not a power of two greater than the previous element, start a new subset
        else:
            if len(current_subset) > len(max_subset):
                max_subset = current_subset
            current_subset = [element]
        previous_element = element
    
    # Add the last element to the current subset if it is a power of two greater than the previous element
    if previous_element is not None and element == previous_element * 2:
        current_subset.append(element)
    
    # If the current subset has more elements than the max subset, update the max subset
    if len(current_subset) > len(max_subset):
        max_subset = current_subset
    
    return max_subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(len(get_max_subset(x)))
    print(" ".join(map(str, get_max_subset(x))))

if __name__ == '__main__':
    main()

