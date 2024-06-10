
def get_unique_detachments(n, k, beauties):
    # Sort the beauties in non-decreasing order
    beauties.sort()
    
    # Initialize the detachments as empty
    detachments = []
    
    # Loop through each day of the pageant
    for day in range(k):
        # Get the beauty of the current detachment
        current_beauty = sum(beauties[day:day+1])
        
        # Find the index of the first soldier with the current beauty
        index = beauties.index(current_beauty)
        
        # Add the soldier to the current detachment
        detachments.append([index+1])
        
        # Remove the soldier from the list of beauties
        beauties.pop(index)
    
    return detachments

def main():
    n, k = map(int, input().split())
    beauties = list(map(int, input().split()))
    detachments = get_unique_detachments(n, k, beauties)
    for detachment in detachments:
        print(len(detachment), *detachment)

if __name__ == '__main__':
    main()

