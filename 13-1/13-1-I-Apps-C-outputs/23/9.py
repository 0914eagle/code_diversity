
def f1(n, s):
    # Initialize variables
    tellers = []
    votes1 = 0
    votes2 = 0
    swaps = 0

    # Find the tellers and their indices
    for i in range(n):
        if s[i] == "0":
            tellers.append(i)

    # Iterate through the citizens and count the votes
    for i in range(n):
        if s[i] == "1":
            votes1 += 1
        elif s[i] == "2":
            votes2 += 1

    # If one party has more votes than the other, return the minimum number of swaps necessary
    if votes1 > votes2:
        return swaps
    elif votes2 > votes1:
        return swaps + 1

    # If both parties have the same number of votes, try swapping the tellers with their adjacent citizens
    for i in range(len(tellers)):
        teller_idx = tellers[i]
        if i + 1 < len(tellers):
            next_teller_idx = tellers[i + 1]
            if s[teller_idx] == s[next_teller_idx]:
                swaps += 1
                s = s[:teller_idx] + s[next_teller_idx] + s[teller_idx + 1:]
        if i - 1 >= 0:
            prev_teller_idx = tellers[i - 1]
            if s[teller_idx] == s[prev_teller_idx]:
                swaps += 1
                s = s[:prev_teller_idx] + s[teller_idx] + s[prev_teller_idx + 1:]

    # If the swap was successful, return the minimum number of swaps necessary
    if votes1 > votes2:
        return swaps
    elif votes2 > votes1:
        return swaps + 1

    # If the swap was unsuccessful, return "impossible"
    return "impossible"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

