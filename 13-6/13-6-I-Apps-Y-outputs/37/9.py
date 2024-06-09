
def has_palindrome_subsequence(a):
    # Base case: if the input array has only one element, return False
    if len(a) == 1:
        return False
    
    # Initialize a set to store the indices of the elements in the input array
    indices = set()
    
    # Iterate over the elements in the input array
    for i in range(len(a)):
        # If the current element is already in the set, skip it
        if i in indices:
            continue
        # If the current element is the middle element of a palindrome, return True
        if i > 0 and i < len(a) - 1 and a[i] == a[i - 1] == a[i + 1]:
            return True
        # If the current element is the first element of a palindrome, add the indices of the next two elements to the set
        if i < len(a) - 2 and a[i] == a[i + 1] == a[i + 2]:
            indices.add(i + 1)
            indices.add(i + 2)
    
    # If no palindrome has been found, return False
    return False

def has_palindrome_subsequence_2(a):
    # Base case: if the input array has only one element, return False
    if len(a) == 1:
        return False
    
    # Initialize a set to store the indices of the elements in the input array
    indices = set()
    
    # Iterate over the elements in the input array
    for i in range(len(a)):
        # If the current element is already in the set, skip it
        if i in indices:
            continue
        # If the current element is the middle element of a palindrome, return True
        if i > 0 and i < len(a) - 1 and a[i] == a[i - 1] == a[i + 1]:
            return True
        # If the current element is the first element of a palindrome, add the indices of the next two elements to the set
        if i < len(a) - 2 and a[i] == a[i + 1] == a[i + 2]:
            indices.add(i + 1)
            indices.add(i + 2)
    
    # If no palindrome has been found, return False
    return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES") if has_palindrome_subsequence(a) else print("NO")

