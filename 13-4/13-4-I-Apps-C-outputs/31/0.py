
def pre_print(t):
    output(t.value)
    if t.left != null: pre_print(t.left)
    if t.right != null: pre_print(t.right)

def in_print(t):
    if t.left != null: pre_print(t.left)
    output(t.value)
    if t.right != null: pre_print(t.right)

def post_print(t):
    if t.left != null: pre_print(t.left)
    if t.right != null: pre_print(t.right)
    output(t.value)

def main():
    pre_output = input("Enter the observed output of the prePrint routine: ")
    in_output = input("Enter the observed output of the inPrint routine: ")
    post_output = input("Enter the observed output of the postPrint routine: ")

    # Your code here

if __name__ == '__main__':
    main()

