
def get_party_members(input_list):
    party_members = {}
    for mp in input_list:
        if mp not in party_members:
            party_members[mp] = 'A'
        else:
            party_members[mp] = 'B'
    return party_members

def solve(n, monday, tuesday, wednesday, thursday, friday):
    party_members = {}
    for day in [monday, tuesday, wednesday, thursday, friday]:
        for pair in day:
            mp1, mp2 = pair
            if mp1 not in party_members:
                party_members[mp1] = 'A'
            if mp2 not in party_members:
                party_members[mp2] = 'B'
            if party_members[mp1] == party_members[mp2]:
                party_members[mp1] = 'A'
                party_members[mp2] = 'B'
    return "".join(party_members[i] for i in range(1, n+1))

if __name__ == '__main__':
    n = int(input())
    monday = list(map(int, input().split()))
    tuesday = list(map(int, input().split()))
    wednesday = list(map(int, input().split()))
    thursday = list(map(int, input().split()))
    friday = list(map(int, input().split()))
    print(solve(n, monday, tuesday, wednesday, thursday, friday))

