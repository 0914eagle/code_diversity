
def get_ant_order(first_row, second_row, t):
    # Initialize the order of the ants
    ant_order = first_row + second_row

    # Iterate over the time steps
    for i in range(t):
        # Find the indices of the ants that need to switch places
        switch_indices = [i for i in range(len(ant_order)) if i % 2 == 0]

        # Switch the places of the ants at the corresponding indices
        for index in switch_indices:
            ant_order[index], ant_order[index + 1] = ant_order[index + 1], ant_order[index]

    return "".join(ant_order)

def main():
    first_row, second_row, t = map(str, input().split())
    print(get_ant_order(first_row, second_row, int(t)))

if __name__ == '__main__':
    main()

