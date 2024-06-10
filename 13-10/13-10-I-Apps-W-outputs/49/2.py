
def is_solution_possible(tshirt_sizes, participants):
    # Initialize a dictionary to store the tshirt sizes and their counts
    tshirt_counts = {}
    for size in tshirt_sizes:
        tshirt_counts[size] = tshirt_sizes[size]

    # Iterate through the participants and deduct the tshirt counts
    for participant in participants:
        if len(participant) == 1:
            if tshirt_counts[participant[0]] > 0:
                tshirt_counts[participant[0]] -= 1
            else:
                return False
        elif len(participant) == 2:
            if tshirt_counts[participant[0]] > 0 and tshirt_counts[participant[1]] > 0:
                tshirt_counts[participant[0]] -= 1
                tshirt_counts[participant[1]] -= 1
            else:
                return False
        else:
            return False

    # If all tshirts are assigned, return True
    return True

def get_solution(tshirt_sizes, participants):
    # Initialize a dictionary to store the tshirt sizes and their counts
    tshirt_counts = {}
    for size in tshirt_sizes:
        tshirt_counts[size] = tshirt_sizes[size]

    # Iterate through the participants and deduct the tshirt counts
    solution = []
    for participant in participants:
        if len(participant) == 1:
            if tshirt_counts[participant[0]] > 0:
                tshirt_counts[participant[0]] -= 1
                solution.append(participant[0])
            else:
                return False
        elif len(participant) == 2:
            if tshirt_counts[participant[0]] > 0 and tshirt_counts[participant[1]] > 0:
                tshirt_counts[participant[0]] -= 1
                tshirt_counts[participant[1]] -= 1
                solution.append(participant[0])
            else:
                return False
        else:
            return False

    # If all tshirts are assigned, return the solution
    return solution

def main():
    tshirt_sizes = input()
    participants = input()
    if is_solution_possible(tshirt_sizes, participants):
        solution = get_solution(tshirt_sizes, participants)
        print("YES")
        for participant in solution:
            print(participant)
    else:
        print("NO")

if __name__ == '__main__':
    main()

