
def get_stairways(numbers):
    stairways = []
    current_stairway = []
    for number in numbers:
        if number == 1:
            stairways.append(current_stairway)
            current_stairway = []
        else:
            current_stairway.append(number)
    
    return stairways

def get_steps_in_stairway(stairway):
    return len(stairway)

def get_number_of_stairways(numbers):
    stairways = get_stairways(numbers)
    return len(stairways)

def get_steps_in_each_stairway(numbers):
    stairways = get_stairways(numbers)
    return [get_steps_in_stairway(stairway) for stairway in stairways]

def main():
    numbers = [int(x) for x in input().split()]
    print(get_number_of_stairways(numbers))
    print(*get_steps_in_each_stairway(numbers))

if __name__ == "__main__":
    main()

