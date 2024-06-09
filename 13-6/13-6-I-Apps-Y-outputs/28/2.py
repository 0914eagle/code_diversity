
def solve(n, words):
    count = 0
    for word in words:
        if word.isdigit():
            count += 1
        elif word == "mumble":
            return "something is fishy"
    return "makes sense" if count == n else "something is fishy"

