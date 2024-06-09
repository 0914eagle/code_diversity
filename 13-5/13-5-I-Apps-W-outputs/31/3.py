
def get_min_jury_size(n, olympiads):
    # Initialize a set to store the dates of the Olympiads
    dates = set()
    # Iterate over the list of Olympiads
    for olymp in olympiads:
        # Add the dates of the Olympiad to the set
        dates.update(range(olymp[1], olymp[1] + olymp[3]))
    # Return the length of the set, which is the minimum jury size
    return len(dates)

def main():
    # Read the number of Olympiads
    n = int(input())
    # Read the information about the Olympiads
    olympiads = []
    for i in range(n):
        olympiads.append(list(map(int, input().split())))
    # Call the function to get the minimum jury size
    min_jury_size = get_min_jury_size(n, olympiads)
    # Print the result
    print(min_jury_size)

if __name__ == '__main__':
    main()

