
def generate_essay(A, B):
    essay = ""
    for i in range(A):
        word = ""
        for j in range(B):
            word += chr(ord('a') + j % 26)
        essay += word + " "
    return essay.strip()

