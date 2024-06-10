
def get_detachments(soldiers, k):
    # Initialize a set to store the sent beauties
    sent_beauties = set()
    # Initialize a list to store the detachments
    detachments = []
    # Loop through the soldiers
    for soldier in soldiers:
        # Check if the soldier's beauty is not already sent
        if soldier["beauty"] not in sent_beauties:
            # Add the soldier's beauty to the set of sent beauties
            sent_beauties.add(soldier["beauty"])
            # Add the soldier to the detachment
            detachments.append([soldier])
            # Decrement the number of days left
            k -= 1
            # Check if all days have been sent
            if k == 0:
                # Return the detachments
                return detachments
    # If the loop completes and there are still days left, it means that not all soldiers can be sent
    # So, return an empty list
    return []

def get_solution(soldiers, k):
    # Initialize a list to store the solutions
    solutions = []
    # Loop through the soldiers
    for soldier in soldiers:
        # Get the detachments for the current soldier
        detachments = get_detachments(soldiers, k)
        # Check if the detachments are not empty
        if detachments:
            # Add the detachments to the solutions
            solutions.append(detachments)
    # Return the solutions
    return solutions

def main():
    # Read the input
    n, k = map(int, input().split())
    soldiers = []
    for i in range(n):
        soldiers.append({"beauty": int(input())})
    # Get the solutions
    solutions = get_solution(soldiers, k)
    # Print the solutions
    for solution in solutions:
        for detachment in solution:
            print(len(detachment), *[soldier["beauty"] for soldier in detachment])

if __name__ == '__main__':
    main()

