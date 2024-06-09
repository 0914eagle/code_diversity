
def f1(d, t, s):
    time_to_reach = d / s
    if time_to_reach <= t:
        return "Yes"
    else:
        return "No"

def f2(...):
    # function to calculate the time it takes to reach the place
    # based on the distance and speed
    return ...

if __name__ == '__main__':
    d, t, s = map(int, input().split())
    print(f1(d, t, s))

