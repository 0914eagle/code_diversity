
def solve(s):
    count = 0
    while "bulbasaur" in s:
        s = s.replace("Bulbasaur", "", 1)
        count += 1
    return count

