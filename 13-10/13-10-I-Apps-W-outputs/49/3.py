
def get_input():
    tshirt_sizes = input().split()
    n = int(input())
    participants = []
    for i in range(n):
        participants.append(input())
    return tshirt_sizes, n, participants

def is_valid_distribution(tshirt_sizes, n, participants):
    total_tshirts = sum(int(tshirt_sizes[i]) for i in range(len(tshirt_sizes)))
    if total_tshirts < n:
        return False
    
    for participant in participants:
        if ',' in participant:
            size1, size2 = participant.split(',')
            if tshirt_sizes[ord(size1) - ord('S')] == 0 and tshirt_sizes[ord(size2) - ord('S')] == 0:
                return False
        else:
            if tshirt_sizes[ord(participant) - ord('S')] == 0:
                return False
    
    return True

def get_distribution(tshirt_sizes, n, participants):
    distribution = []
    for participant in participants:
        if ',' in participant:
            size1, size2 = participant.split(',')
            if tshirt_sizes[ord(size1) - ord('S')] > 0:
                distribution.append(size1)
                tshirt_sizes[ord(size1) - ord('S')] -= 1
            else:
                distribution.append(size2)
                tshirt_sizes[ord(size2) - ord('S')] -= 1
        else:
            distribution.append(participant)
            tshirt_sizes[ord(participant) - ord('S')] -= 1
    
    return distribution

def main():
    tshirt_sizes, n, participants = get_input()
    if is_valid_distribution(tshirt_sizes, n, participants):
        distribution = get_distribution(tshirt_sizes, n, participants)
        print("YES")
        print(*distribution, sep='\n')
    else:
        print("NO")

if __name__ == '__main__':
    main()

