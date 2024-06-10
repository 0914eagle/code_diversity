
def get_t_shirt_sizes(n):
    t_shirt_sizes = []
    for i in range(n):
        size = input()
        t_shirt_sizes.append(size)
    return t_shirt_sizes

def get_t_shirt_counts(n):
    t_shirt_counts = []
    for i in range(n):
        count = input()
        t_shirt_counts.append(count)
    return t_shirt_counts

def can_present_t_shirts(t_shirt_sizes, t_shirt_counts):
    # Check if it is possible to present a t-shirt to each participant
    # Return True if it is possible, False otherwise
    pass

def find_t_shirt_distribution(t_shirt_sizes, t_shirt_counts):
    # Find any valid distribution of the t-shirts
    # Return a list of t-shirt sizes that can be given to the participants
    pass

def main():
    n = int(input())
    t_shirt_sizes = get_t_shirt_sizes(n)
    t_shirt_counts = get_t_shirt_counts(n)
    if can_present_t_shirts(t_shirt_sizes, t_shirt_counts):
        print("YES")
        t_shirt_distribution = find_t_shirt_distribution(t_shirt_sizes, t_shirt_counts)
        for size in t_shirt_distribution:
            print(size)
    else:
        print("NO")

if __name__ == '__main__':
    main()

