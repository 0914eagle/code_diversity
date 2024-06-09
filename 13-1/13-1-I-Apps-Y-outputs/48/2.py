
def solve(numbers):
    stairways = []
    current_stairway = []
    for number in numbers:
        if number == 1:
            stairways.append(current_stairway)
            current_stairway = []
        else:
            current_stairway.append(number)
    
    return len(stairways), [len(stairway) for stairway in stairways]

