
def get_candy_values(a_values, b_values):
    # Initialize variables
    alf_candy_values = []
    beata_candy_values = []
    candy_values = a_values + b_values

    # Sort the candy values in descending order
    candy_values.sort(reverse=True)

    # Loop through the candy values and assign them to Alf or Beata based on their preferences
    for i in range(len(candy_values)):
        if i % 2 == 0:
            alf_candy_values.append(candy_values[i])
        else:
            beata_candy_values.append(candy_values[i])

    # Return the final list of candy values for Alf and Beata
    return alf_candy_values, beata_candy_values

def get_candy_assignment(alf_candy_values, beata_candy_values):
    # Initialize variables
    candy_assignment = []

    # Loop through the candy values and assign them to Alf or Beata based on their preferences
    for i in range(len(alf_candy_values)):
        if alf_candy_values[i] > beata_candy_values[i]:
            candy_assignment.append("A")
        else:
            candy_assignment.append("B")

    # Return the final list of candy assignments
    return "".join(candy_assignment)

def main():
    # Read the input
    n = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))

    # Call the functions to get the candy values and assignment
    alf_candy_values, beata_candy_values = get_candy_values(a_values, b_values)
    candy_assignment = get_candy_assignment(alf_candy_values, beata_candy_values)

    # Print the output
    print(candy_assignment)

if __name__ == '__main__':
    main()

