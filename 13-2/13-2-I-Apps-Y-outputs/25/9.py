
def is_connected(S):
    # Check if there is a pair of stations that will be connected by a bus service
    if S[0] == "A" and S[2] == "B":
        return True
    elif S[0] == "B" and S[2] == "A":
        return True
    else:
        return False

if __name__ == '__main__':
    S = input()
    print(is_connected(S))

