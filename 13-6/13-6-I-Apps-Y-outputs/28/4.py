
def check_counting(n, words):
    count = 0
    for word in words:
        if word.isdigit():
            count += 1
        elif word == "mumble":
            return "something is fishy"
    if count == n:
        return "makes sense"
    else:
        return "something is fishy"

