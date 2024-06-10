
def get_min_minutes(hamsters_list):
    # Find the number of standing and sitting hamsters
    num_standing = hamsters_list.count('X')
    num_sitting = hamsters_list.count('x')

    # Find the minimum number of minutes needed to get the required number of standing hamsters
    min_minutes = (num_standing // 2) // num_sitting

    return min_minutes

def get_final_hamsters_list(hamsters_list, min_minutes):
    # Create a copy of the original hamsters list
    final_hamsters_list = hamsters_list[:]

    # Iterate through the hamsters list and change the position of the hamsters based on the minimum number of minutes needed
    for i in range(min_minutes):
        for j in range(len(hamsters_list)):
            if hamsters_list[j] == 'x':
                final_hamsters_list[j] = 'X'
            else:
                final_hamsters_list[j] = 'x'

    return final_hamsters_list

if __name__ == '__main__':
    hamsters_list = input()
    min_minutes = get_min_minutes(hamsters_list)
    final_hamsters_list = get_final_hamsters_list(hamsters_list, min_minutes)
    print(min_minutes)
    print(''.join(final_hamsters_list))

