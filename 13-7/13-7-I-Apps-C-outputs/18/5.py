
def get_max_executives(num_briefcases, briefcase_contents):
    # Sort the briefcase contents in descending order
    sorted_briefcase_contents = sorted(briefcase_contents, reverse=True)

    # Initialize the number of executives to reward as 0
    num_executives = 0

    # Loop through the sorted briefcase contents and assign each briefcase to the least evil executive
    for i in range(len(sorted_briefcase_contents)):
        # If the current briefcase content is greater than or equal to the total number of bananas received by the current executive, give the current briefcase to the current executive
        if sorted_briefcase_contents[i] >= sum(briefcase_contents[:num_executives]):
            num_executives += 1

    return num_executives

def main():
    num_briefcases = int(input())
    briefcase_contents = list(map(int, input().split()))
    print(get_max_executives(num_briefcases, briefcase_contents))

if __name__ == '__main__':
    main()

