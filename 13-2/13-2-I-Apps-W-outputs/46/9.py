
def f1(t, pieces):
    # convert the pieces to a set to remove duplicates
    pieces = set(pieces)
    # count the number of instances of t in the pieces
    count = pieces.count(t)
    # return the count
    return count

def f2(t, pieces):
    # convert the pieces to a list to be able to modify it
    pieces = list(pieces)
    # count the number of instances of t in the pieces
    count = pieces.count(t)
    # iterate over the pieces and check if they are similar to t
    for i in range(len(pieces)):
        if pieces[i] in [6, 9]:
            # if the piece is similar to t, replace it with t
            pieces[i] = t
            # increment the count
            count += 1
    # return the count
    return count

if __name__ == '__main__':
    t = int(input())
    pieces = input()
    print(f2(t, pieces))

