
def get_max_score(numbers):
    
    # Initialize the score and the current group of numbers
    score = 0
    group = numbers
    
    # While the group has more than one number, split it into two non-empty groups and give them to Toastman
    while len(group) > 1:
        # Split the group into two non-empty groups
        group1, group2 = split_group(group)
        
        # Add the sum of the current group to the score
        score += sum(group)
        
        # Give the groups to Appleman
        group = [group1, group2]
    
    # If the group has only one number, throw it out
    if len(group) == 1:
        score += group[0]
    
    return score

def split_group(group):
    
    # Initialize the two groups
    group1 = []
    group2 = []
    
    # Split the group into two non-empty groups
    for i in range(len(group)):
        if i % 2 == 0:
            group1.append(group[i])
        else:
            group2.append(group[i])
    
    return group1, group2

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(int(input()))]
    print(get_max_score(numbers))

