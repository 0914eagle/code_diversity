
import random

def get_distinct_integers(expression):
    integers = []
    for token in expression.split("+"):
        integers.append(int(token))
    
    distinct_integers = set()
    for i in range(len(integers)):
        for j in range(i+1, len(integers)):
            if random.randint(0, 1) == 0:
                distinct_integers.add(integers[i] + integers[j])
            else:
                distinct_integers.add(str(integers[i]) + str(integers[j]))
    
    return len(distinct_integers)

def main():
    expression = input("Enter an expression: ")
    print(get_distinct_integers(expression))

if __name__ == '__main__':
    main()

