
def get_sequence_length(confusion, length):
    # Base case: if the length of the sequence is 1, there is only one sequence with that length and confusion
    if length == 1:
        return 1
    
    # Recursive case: if the length of the sequence is greater than 1, there are two cases to consider
    # Case 1: the first number in the sequence is smaller than the last number
    # Case 2: the first number in the sequence is larger than the last number
    return get_sequence_length(confusion-1, length-1) + get_sequence_length(confusion, length-1)

def get_number_of_sequences(length, confusion):
    # Calculate the number of sequences with the given length and confusion
    return get_sequence_length(confusion, length)

if __name__ == '__main__':
    N, C = map(int, input().split())
    print(get_number_of_sequences(N, C) % 1000000007)

