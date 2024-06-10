
def get_monotonic_renumbering_count(n, a):
    # Initialize a dictionary to store the counts of monotonic renumberings
    count_dict = {}
    
    # Iterate over the elements of the array
    for i in range(n):
        # If the element is not already in the dictionary, add it with a count of 1
        if a[i] not in count_dict:
            count_dict[a[i]] = 1
        # If the element is already in the dictionary, increment its count
        else:
            count_dict[a[i]] += 1
    
    # Initialize a variable to store the total number of monotonic renumberings
    total_count = 1
    
    # Iterate over the keys of the dictionary
    for key in count_dict:
        # If the count of the current key is greater than 1, add the number of ways it can be renumbered to the total count
        if count_dict[key] > 1:
            total_count *= count_dict[key]
    
    # Return the total count modulo 998244353
    return total_count % 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_monotonic_renumbering_count(n, a))

if __name__ == '__main__':
    main()

