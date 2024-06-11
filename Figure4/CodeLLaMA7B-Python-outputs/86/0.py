def anti_shuffle(s):
    
    if s == "":
        return s
    else:
        return " ".join(sorted(s.split(), key=lambda x: "".join(sorted(x))))


if __name__ == '__main__':
    print(anti_shuffle("Hello World!!!"))
