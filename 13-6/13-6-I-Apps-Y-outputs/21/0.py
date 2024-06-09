
def is_shiritori(words):
    if len(words) == 0:
        return True
    seen = set()
    for word in words:
        if word in seen:
            return False
        seen.add(word)
    return True

def main():
    num_words = int(input())
    words = []
    for i in range(num_words):
        words.append(input())
    if is_shiritori(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

