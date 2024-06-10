
def get_unique_beauties(n, k, beauties):
    # Sort the beauties in ascending order
    sorted_beauties = sorted(beauties)
    # Initialize an empty list to store the selected beauties
    selected_beauties = []
    # Loop through the days of the pageant
    for day in range(k):
        # Get the current day's beauty
        current_beauty = sum(sorted_beauties[:day+1])
        # Check if the current day's beauty is already selected
        if current_beauty not in selected_beauties:
            # If not, select it and add it to the list of selected beauties
            selected_beauties.append(current_beauty)
        # If the current day's beauty is already selected, find the next day's beauty that is not selected yet
        else:
            for i in range(day+1, n):
                if sorted_beauties[i] not in selected_beauties:
                    selected_beauties.append(sorted_beauties[i])
                    break
    return selected_beauties

def get_detachments(n, k, beauties, selected_beauties):
    # Initialize an empty list to store the detachments
    detachments = []
    # Loop through the days of the pageant
    for day in range(k):
        # Get the current day's beauty
        current_beauty = selected_beauties[day]
        # Find the number of soldiers in the detachment for the current day
        num_soldiers = 0
        for beauty in beauties:
            if beauty <= current_beauty:
                num_soldiers += 1
        # Create a list of soldiers with the current day's beauty
        soldiers = []
        for i in range(num_soldiers):
            soldiers.append(beauties[i])
        # Add the detachment to the list of detachments
        detachments.append(soldiers)
    return detachments

def main():
    n, k = map(int, input().split())
    beauties = list(map(int, input().split()))
    selected_beauties = get_unique_beauties(n, k, beauties)
    detachments = get_detachments(n, k, beauties, selected_beauties)
    for detachment in detachments:
        print(len(detachment), *detachment)

if __name__ == '__main__':
    main()

