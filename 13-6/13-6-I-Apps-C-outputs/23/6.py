
def get_average_length(sequence):
    # Initialize variables
    num_h = sequence.count('H')
    num_t = sequence.count('T')
    num_unknown = sequence.count('?')
    length = 0
    num_configurations = 0
    
    # Iterate over all possible configurations
    for i in range(1 << num_unknown):
        configuration = []
        for j in range(num_h):
            configuration.append('H')
        for j in range(num_t):
            configuration.append('T')
        for j in range(num_unknown):
            if i & (1 << j):
                configuration.append('H')
            else:
                configuration.append('T')
        length += get_length(configuration)
        num_configurations += 1
    
    # Return the average length
    return length / num_configurations

def get_length(configuration):
    # Initialize variables
    num_h = configuration.count('H')
    num_t = configuration.count('T')
    length = 0
    
    # Iterate over all possible operations
    for i in range(num_h):
        if configuration[i] == 'H':
            length += 1
        else:
            break
    for i in range(num_t):
        if configuration[i] == 'T':
            length += 1
        else:
            break
    
    # Return the length
    return length

if __name__ == '__main__':
    sequence = input()
    print(get_average_length(sequence))

