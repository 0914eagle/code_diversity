
def is_rated(participants):
    # Check if at least one participant's rating has changed
    if len(set([participant[0] for participant in participants])) < len(participants):
        return "rated"
    
    # Check if the round was rated and a participant with lower rating took a better place in the standings than a participant with higher rating
    for i in range(1, len(participants)):
        if participants[i][0] < participants[i-1][0] and participants[i][1] > participants[i-1][1]:
            return "rated"
    
    # If none of the above conditions are met, it's impossible to determine whether the round is rated or not
    return "maybe"

def main():
    n = int(input())
    participants = []
    for i in range(n):
        participants.append(list(map(int, input().split())))
    print(is_rated(participants))

if __name__ == '__main__':
    main()

