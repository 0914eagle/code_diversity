
def get_replacement_sequence(a, b):
    # Initialize a dictionary to keep track of the elements in b
    element_dict = {}
    for element in b:
        element_dict[element] = 0

    # Initialize a list to store the resulting sequence
    result = []

    # Iterate through the elements in a
    for element in a:
        # If the element is 0, replace it with an element from b
        if element == 0:
            # Find the first unused element in b
            for i in range(1, len(b) + 1):
                if element_dict[i] == 0:
                    result.append(i)
                    element_dict[i] = 1
                    break
        # If the element is not 0, add it to the resulting sequence
        else:
            result.append(element)

    return result

def is_increasing_sequence(sequence):
    # Check if the sequence is increasing
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = get_replacement_sequence(a, b)

    if is_increasing_sequence(result):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

