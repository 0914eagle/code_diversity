
def execute_statement(statement):
    x = 0
    for char in statement:
        if char == '+':
            x += 1
        elif char == '-':
            x -= 1
    return x

def execute_programme(programme):
    x = 0
    for statement in programme:
        x = execute_statement(statement)
    return x

if __name__ == '__main__':
    n = int(input())
    programme = []
    for _ in range(n):
        programme.append(input())
    print(execute_programme(programme))

