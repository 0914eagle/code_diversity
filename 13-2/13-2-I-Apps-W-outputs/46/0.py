
def f1(t, pieces):
    # convert the pieces to a set to remove duplicates
    pieces = set(pieces)
    # count the number of instances of t in the pieces
    count = pieces.count(t)
    # if t is not in the pieces, return 0
    if count == 0:
        return 0
    # if t is in the pieces, return the count
    return count

def f2(t, pieces):
    # convert the pieces to a set to remove duplicates
    pieces = set(pieces)
    # count the number of instances of t in the pieces
    count = pieces.count(t)
    # if t is not in the pieces, return 0
    if count == 0:
        return 0
    # if t is in the pieces, return the count
    return count

if __name__ == '__main__':
    t = int(input())
    pieces = input()
    print(f1(t, pieces))
    print(f2(t, pieces))

