
def is_good(seq):
    # Check if the sequence is empty
    if not seq:
        return True
    
    # Check if any two elements in the sequence sum to a power of two
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if is_power_of_two(seq[i] + seq[j]):
                return True
    
    # If we reach this point, none of the pairs in the sequence sum to a power of two
    return False

def is_power_of_two(n):
    return n > 0 and bin(n).count('1') == 1

def get_min_elements_to_remove(seq):
    # Find the minimum number of elements needed to remove to make the sequence good
    min_elements_to_remove = len(seq)
    for i in range(len(seq)):
        seq_copy = seq[:]
        seq_copy.pop(i)
        if is_good(seq_copy):
            min_elements_to_remove = min(min_elements_to_remove, len(seq) - len(seq_copy))
    
    return min_elements_to_remove

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(get_min_elements_to_remove(seq))

