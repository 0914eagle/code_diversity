
def get_council_members(n, residents):
    council_members = []
    for resident in residents:
        if resident[1] not in council_members:
            council_members.append(resident[1])
    return council_members

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        residents = []
        for j in range(n):
            resident = input().split()
            residents.append(resident)
        council_members = get_council_members(n, residents)
        for council_member in council_members:
            print(council_member)
        print()

if __name__ == '__main__':
    main()

