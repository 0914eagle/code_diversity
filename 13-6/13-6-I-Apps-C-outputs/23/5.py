
def f1(s):
    # function to calculate the average value of L(C) for a given sequence S
    # calculate the number of operations for each possible initial state and sum them up
    # divide the sum by the number of possible initial states to get the average
    num_ops = 0
    for i in range(len(s)):
        if s[i] == "H":
            num_ops += 1
        elif s[i] == "?":
            num_ops += 2
    return num_ops / len(s)

def f2(s):
    # function to calculate the average value of L(C) for a given sequence S
    # calculate the number of operations for each possible initial state and sum them up
    # divide the sum by the number of possible initial states to get the average
    num_ops = 0
    for i in range(len(s)):
        if s[i] == "H":
            num_ops += 1
        elif s[i] == "?":
            num_ops += 2
    return num_ops / len(s)

if __name__ == '__main__':
    s = input()
    print(f1(s))
    print(f2(s))

