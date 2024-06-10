
def is_valid_distribution(t_shirts, participants):
    # Initialize a dictionary to store the number of t-shirts of each size
    t_shirts_dict = {}
    for size, count in enumerate(t_shirts):
        t_shirts_dict[size] = count

    # Iterate through the participants and check if they can get a t-shirt of proper size
    for participant in participants:
        if len(participant) == 1:
            # Check if there is at least one t-shirt of the participant's size
            if t_shirts_dict[participant[0]] == 0:
                return False
            else:
                t_shirts_dict[participant[0]] -= 1
        else:
            # Check if there is at least one t-shirt of the participant's first size
            if t_shirts_dict[participant[0]] == 0:
                return False
            # Check if there is at least one t-shirt of the participant's second size
            if t_shirts_dict[participant[1]] == 0:
                return False
            t_shirts_dict[participant[0]] -= 1
            t_shirts_dict[participant[1]] -= 1

    return True

def get_solution(t_shirts, participants):
    # Initialize a dictionary to store the number of t-shirts of each size
    t_shirts_dict = {}
    for size, count in enumerate(t_shirts):
        t_shirts_dict[size] = count

    # Initialize a list to store the solution
    solution = []

    # Iterate through the participants and find a valid distribution of t-shirts
    for participant in participants:
        if len(participant) == 1:
            # Find a t-shirt of the participant's size
            for size in range(participant[0], len(t_shirts)):
                if t_shirts_dict[size] > 0:
                    solution.append(size)
                    t_shirts_dict[size] -= 1
                    break
        else:
            # Find a t-shirt of the participant's first size
            for size in range(participant[0], len(t_shirts)):
                if t_shirts_dict[size] > 0:
                    solution.append(size)
                    t_shirts_dict[size] -= 1
                    break
            # Find a t-shirt of the participant's second size
            for size in range(participant[1], len(t_shirts)):
                if t_shirts_dict[size] > 0:
                    solution.append(size)
                    t_shirts_dict[size] -= 1
                    break

    return solution

def main():
    t_shirts = [int(x) for x in input().split()]
    n = int(input())
    participants = [list(map(int, input().split(','))) for _ in range(n)]

    if is_valid_distribution(t_shirts, participants):
        print("YES")
        print("\n".join(str(x) for x in get_solution(t_shirts, participants)))
    else:
        print("NO")

if __name__ == '__main__':
    main()

