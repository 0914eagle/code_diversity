
def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def solve(n, k, a):
    # Create a set to store the sent beauties
    sent_beauties = set()
    # Create a list to store the selected soldiers
    selected_soldiers = []
    # Iterate through the days
    for day in range(k):
        # Find the soldier with the maximum beauty
        max_beauty = max(a)
        # Find the index of the soldier with the maximum beauty
        max_index = a.index(max_beauty)
        # Add the soldier to the selected soldiers list
        selected_soldiers.append(max_index)
        # Remove the soldier from the list
        a.pop(max_index)
        # Add the beauty of the sent detachment to the set
        sent_beauties.add(sum(selected_soldiers))
        # If the set size is equal to the number of days, we have found a solution
        if len(sent_beauties) == k:
            break
    # Return the selected soldiers
    return selected_soldiers

def get_output(selected_soldiers):
    output = ""
    # Iterate through the days
    for day in range(len(selected_soldiers)):
        # Get the soldier at the current day
        soldier = selected_soldiers[day]
        # Add the soldier to the output
        output += str(soldier) + " "
    return output.strip()

if __name__ == '__main__':
    n, k, a = get_input()
    selected_soldiers = solve(n, k, a)
    print(get_output(selected_soldiers))

