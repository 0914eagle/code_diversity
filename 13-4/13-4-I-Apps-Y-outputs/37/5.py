
import re

def is_eastern_gothic(sentence):
    pattern = re.compile(r'ae')
    match = pattern.search(sentence)
    if match:
        return True
    else:
        return False

def main():
    sentence = input()
    if is_eastern_gothic(sentence):
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

if __name__ == "__main__":
    main()

