
import sys

def get_inconvenience(bridges, collapsed_bridges):
    inconvenience = 0
    for bridge in bridges:
        if bridge[0] in collapsed_bridges or bridge[1] in collapsed_bridges:
            inconvenience += 1
    return inconvenience

def main():
    n, m = map(int, input().split())
    bridges = []
    for _ in range(m):
        a, b = map(int, input().split())
        bridges.append((a, b))
    
    collapsed_bridges = set()
    for i in range(m):
        collapsed_bridges.add(i+1)
        inconvenience = get_inconvenience(bridges, collapsed_bridges)
        print(inconvenience)

if __name__ == "__main__":
    main()

