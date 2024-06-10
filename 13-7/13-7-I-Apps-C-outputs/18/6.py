
def get_max_executives(briefcase_count, briefcase_values):
    # Sort the briefcases in non-decreasing order of value
    sorted_briefcases = sorted(briefcase_values)

    # Initialize the maximum number of executives to be rewarded
    max_executives = 0

    # Loop through the briefcases and reward executives
    for i in range(briefcase_count):
        # Get the value of the current briefcase
        value = sorted_briefcases[i]

        # Calculate the number of executives that can be rewarded with this briefcase
        executives = (briefcase_count - i) // (value + 1)

        # Update the maximum number of executives if necessary
        max_executives = max(max_executives, executives)

    return max_executives

def main():
    briefcase_count = int(input())
    briefcase_values = list(map(int, input().split()))
    print(get_max_executives(briefcase_count, briefcase_values))

if __name__ == '__main__':
    main()

