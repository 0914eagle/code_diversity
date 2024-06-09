
import re

def is_eastern_gothic(sentence):
    pattern = re.compile(r'ae')
    matches = pattern.findall(sentence)
    if len(matches) / len(sentence.split()) >= 0.4:
        return True
    return False

def main():
    sentence = input()
    if is_eastern_gothic(sentence):
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

if __name__ == "__main__":
    main()

