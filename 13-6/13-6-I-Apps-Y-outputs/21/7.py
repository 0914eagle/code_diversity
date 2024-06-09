
def is_shiritori_observed(words):
    seen = set()
    for word in words:
        if word not in seen:
            seen.add(word)
        else:
            return False
    return True

def main():
    num_words = int(input())
    words = []
    for i in range(num_words):
        words.append(input())
    if is_shiritori_observed(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

