
def get_min_jury_size(n, olympiads):
    # Initialize a set to store the dates of the olympiads
    dates = set()
    # Iterate over the list of olympiads
    for olympiade in olympiads:
        # Add the dates of the olympiad to the set
        dates.update(range(olympiade[0], olympiade[0] + olympiade[3]))
    # Return the length of the set, which is the minimum number of people needed for the jury
    return len(dates)

def main():
    # Read the number of olympiads and the list of olympiads from stdin
    n = int(input())
    olympiads = []
    for i in range(n):
        olympiads.append(list(map(int, input().split())))
    # Call the function to get the minimum jury size and print the result
    print(get_min_jury_size(n, olympiads))

if __name__ == '__main__':
    main()

