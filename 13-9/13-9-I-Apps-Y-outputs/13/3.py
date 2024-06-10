
def is_good(seq):
    # Check if the sequence is empty
    if not seq:
        return True
    
    # Check if any two elements in the sequence add up to a power of two
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if is_power_of_two(seq[i] + seq[j]):
                return True
    
    # If we reach this point, it means that no two elements add up to a power of two
    return False

def is_power_of_two(n):
    return (n > 0) and (n & (n - 1) == 0)

def min_elements_to_remove(seq):
    # Find the minimum number of elements needed to be removed to make the sequence good
    count = 0
    for i in range(len(seq)):
        if not is_good(seq[:i] + seq[i+1:]):
            count += 1
    
    return count

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(min_elements_to_remove(seq))

