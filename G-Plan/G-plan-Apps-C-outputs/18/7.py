
def calculate_operations(sequence):
    count_h = sequence.count('H')
    count_t = sequence.count('T')
    count_q = sequence.count('?')
    
    total_count = count_h + count_t + count_q
    avg_operations = 0
    
    if count_q == 0:
        avg_operations = total_count
    else:
        avg_operations = (count_h * 2 + count_t) / (count_h + count_t + count_q)
    
    return avg_operations

if __name__ == "__main__":
    sequence = input().strip()
    print(calculate_operations(sequence))
