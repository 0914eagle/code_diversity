
def get_essay(A, B):
    essay = ""
    for i in range(A):
        essay += chr(ord('a') + i%26)
        if i%15 == 0:
            essay += " "
    return essay

