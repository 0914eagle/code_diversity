
def get_tshirt_sizes(n, tshirt_sizes):
    # Initialize a dictionary to store the tshirt sizes and their counts
    tshirt_counts = {}
    for size in tshirt_sizes:
        if size not in tshirt_counts:
            tshirt_counts[size] = 1
        else:
            tshirt_counts[size] += 1
    
    # Initialize a list to store the participants' tshirt sizes
    participants = []
    
    # Iterate through the participants and add their tshirt sizes to the list
    for _ in range(n):
        size = input()
        if ',' in size:
            sizes = size.split(',')
            participants.append(sizes)
        else:
            participants.append([size])
    
    # Initialize a variable to keep track of the number of tshirts given
    tshirts_given = 0
    
    # Iterate through the participants and give them tshirts
    for participant in participants:
        if len(participant) == 1:
            if participant[0] in tshirt_counts and tshirt_counts[participant[0]] > 0:
                tshirt_counts[participant[0]] -= 1
                tshirts_given += 1
            else:
                return False
        else:
            if participant[0] in tshirt_counts and tshirt_counts[participant[0]] > 0 and participant[1] in tshirt_counts and tshirt_counts[participant[1]] > 0:
                tshirt_counts[participant[0]] -= 1
                tshirt_counts[participant[1]] -= 1
                tshirts_given += 2
            else:
                return False
    
    # If all participants have received tshirts, return True, otherwise return False
    if tshirts_given == n:
        return True
    else:
        return False

def main():
    n = int(input())
    tshirt_sizes = input().split()
    if get_tshirt_sizes(n, tshirt_sizes):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

