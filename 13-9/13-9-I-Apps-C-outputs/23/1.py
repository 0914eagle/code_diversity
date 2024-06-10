
def get_input():
    num_statements = int(input())
    statements = []
    for _ in range(num_statements):
        statements.append(input())
    return statements

def rhyme(word1, word2):
    min_length = min(3, len(word1), len(word2))
    return word1[-min_length:] == word2[-min_length:]

def is_consistent(statements):
    consistent = True
    for i in range(len(statements)):
        for j in range(i+1, len(statements)):
            if statements[i].split()[0] == statements[j].split()[1] and not rhyme(statements[i].split()[0], statements[j].split()[1]):
                consistent = False
                break
            elif statements[i].split()[1] == statements[j].split()[0] and not rhyme(statements[i].split()[1], statements[j].split()[0]):
                consistent = False
                break
    return consistent

def main():
    statements = get_input()
    if is_consistent(statements):
        print("yes")
    else:
        print("wait what?")

if __name__ == '__main__':
    main()

