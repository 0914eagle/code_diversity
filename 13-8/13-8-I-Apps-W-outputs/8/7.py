
def get_maximum_chests(chests, keys):
    # Initialize a dictionary to store the number of chests that can be opened using each key
    key_to_chests = {}
    for key in keys:
        key_to_chests[key] = 0
    
    # Iterate through the chests and increment the number of chests that can be opened using each key
    for chest in chests:
        for key in keys:
            if (chest + key) % 2 == 1:
                key_to_chests[key] += 1
    
    # Return the maximum number of chests that can be opened
    return max(key_to_chests.values())

def main():
    n, m = map(int, input().split())
    chests = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    print(get_maximum_chests(chests, keys))

if __name__ == '__main__':
    main()

