
def get_final_ratings(n, initial_ratings):
    # Sort the initial ratings in descending order
    sorted_ratings = sorted(initial_ratings, reverse=True)
    # Calculate the difference between the highest and lowest ratings
    diff = sorted_ratings[-1] - sorted_ratings[0]
    # Calculate the number of friends that need to be moved to equalize the ratings
    num_friends = diff // 2
    # Create a list to store the final ratings
    final_ratings = [0] * n
    # Assign the same rating to all friends
    for i in range(n):
        final_ratings[i] = sorted_ratings[0]
    # Move the lowest ratings up by 1 for each friend that needs to be moved
    for i in range(num_friends):
        final_ratings[i] += 1
    return final_ratings

def get_match_plan(n, final_ratings):
    # Create a list to store the match plan
    match_plan = []
    # Iterate over the friends in reverse order
    for i in range(n-1, -1, -1):
        # Check if the friend's final rating is not equal to the highest rating
        if final_ratings[i] != final_ratings[-1]:
            # Add the friend to the match plan
            match_plan.append(i)
    return match_plan

def get_match_plan_string(match_plan):
    # Create an empty string to store the match plan
    match_plan_string = ""
    # Iterate over the friends in the match plan
    for i in match_plan:
        # Add a '1' to the string for each friend that is in the match plan
        match_plan_string += "1"
    return match_plan_string

def main():
    n = int(input())
    initial_ratings = list(map(int, input().split()))
    final_ratings = get_final_ratings(n, initial_ratings)
    match_plan = get_match_plan(n, final_ratings)
    match_plan_string = get_match_plan_string(match_plan)
    print(final_ratings)
    print(len(match_plan))
    print(match_plan_string)

if __name__ == '__main__':
    main()

