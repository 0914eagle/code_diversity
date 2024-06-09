
def f1(D, T, S):
    time_to_reach_place = D / S
    if time_to_reach_place <= T:
        return "Yes"
    else:
        return "No"

def f2(...):
    ...

if __name__ == '__main__':
    D, T, S = map(int, input().split())
    print(f1(D, T, S))

