
def get_unique_beauties(beauties, k):
    unique_beauties = set()
    for i in range(k):
        unique_beauties.add(beauties[i])
    return list(unique_beauties)

def get_detachments(beauties, k):
    unique_beauties = get_unique_beauties(beauties, k)
    detachments = []
    for beauty in unique_beauties:
        detachments.append([beauty])
    return detachments

def print_detachments(detachments):
    for detachment in detachments:
        print(len(detachment), *detachment)

def main():
    n, k = map(int, input().split())
    beauties = list(map(int, input().split()))
    detachments = get_detachments(beauties, k)
    print_detachments(detachments)

if __name__ == '__main__':
    main()

