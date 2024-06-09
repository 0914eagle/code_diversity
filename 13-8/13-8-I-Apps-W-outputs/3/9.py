
import sys

def count_seating_arrangements(n, survey):
    # Initialize a set to store the current and desired desk numbers of each engineer
    desk_numbers = set()
    for engineer in survey:
        desk_numbers.add(engineer[0])
        desk_numbers.add(engineer[1])
    
    # Initialize a dictionary to store the number of possible arrangements for each desk number
    arrangements = {desk: 1 for desk in desk_numbers}
    
    # Iterate through the survey and update the number of possible arrangements for each desk number
    for engineer in survey:
        current_desk, desired_desk = engineer
        arrangements[desired_desk] = (arrangements[desired_desk] * (n - 1)) % 1000000007
        arrangements[current_desk] = (arrangements[current_desk] * (n - 1)) % 1000000007
    
    # Return the total number of possible arrangements
    return sum(arrangements.values()) % 1000000007

n = int(input())
survey = []
for _ in range(n):
    survey.append(list(map(int, input().split())))
print(count_seating_arrangements(n, survey))

