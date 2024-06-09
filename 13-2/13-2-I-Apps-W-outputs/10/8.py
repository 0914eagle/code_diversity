
def max_vk(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == "V" and s[i + 1] == "K":
            count += 1
    return count

