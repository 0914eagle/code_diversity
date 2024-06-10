
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
    
    # Find the maximum number of chests that can be opened
    max_chests = 0
    for key in keys:
        max_chests = max(max_chests, key_to_chests[key])
    
    return max_chests

def main():
    n, m = map(int, input().split())
    chests = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    print(get_maximum_chests(chests, keys))

if __name__ == '__main__':
    main()

