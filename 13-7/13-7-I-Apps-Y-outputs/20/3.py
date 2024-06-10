
def get_label_for_round(round_number):
    
    if round_number <= 999:
        return "ABC"
    else:
        return "ABD"

def main():
    round_number = int(input())
    print(get_label_for_round(round_number))

if __name__ == '__main__':
    main()

