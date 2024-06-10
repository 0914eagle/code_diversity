
def get_inspectors(n, d):
    # Calculate the minimum number of inspectors needed
    inspectors = (n + d - 1) // d
    return inspectors

def main():
    # Read the input data
    n, d = map(int, input().split())

    # Calculate the minimum number of inspectors needed
    inspectors = get_inspectors(n, d)

    # Print the result
    print(inspectors)

if __name__ == '__main__':
    main()

