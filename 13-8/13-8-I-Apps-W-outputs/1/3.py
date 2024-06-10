
def get_sequence(n, k, a, b):
    # Initialize a dictionary to keep track of the elements in b
    b_dict = {}
    for i in range(k):
        b_dict[b[i]] = 1
    
    # Initialize a list to store the resulting sequence
    result = []
    
    # Iterate through the elements in a
    for i in range(n):
        if a[i] == 0:
            # If the element is 0, check if there are any elements in b that haven't been used
            if len(b_dict) > 0:
                # If there are unused elements in b, pick the smallest one and use it
                smallest = min(b_dict.keys())
                result.append(smallest)
                b_dict[smallest] += 1
            else:
                # If all elements in b have been used, we can't form an increasing sequence
                return "No"
        else:
            # If the element is not 0, just add it to the resulting sequence
            result.append(a[i])
    
    # Check if the resulting sequence is increasing
    for i in range(n - 1):
        if result[i] >= result[i + 1]:
            return "No"
    
    # If the sequence is increasing, return "Yes"
    return "Yes"

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_sequence(n, k, a, b))

if __name__ == '__main__':
    main()

