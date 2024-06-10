
import math

def get_walk_length(walk):
    return len(walk)

def get_walk_probability(walk, num_rooms):
    probability = 1
    for i in range(num_rooms):
        probability *= (len(walk) - walk.count(i)) / (num_rooms - 1)
    return probability

def get_sentry_probability(num_rooms, num_sentries):
    probability = 1
    for i in range(num_sentries):
        probability *= (num_rooms - 1) / num_rooms
    return probability

def get_capture_probability(walk, num_rooms, num_sentries):
    walk_probability = get_walk_probability(walk, num_rooms)
    sentry_probability = get_sentry_probability(num_rooms, num_sentries)
    return walk_probability * sentry_probability

def main():
    num_rooms = int(input())
    num_sentries = int(input())
    walk = list(map(int, input().split()))
    print(get_capture_probability(walk, num_rooms, num_sentries))

if __name__ == '__main__':
    main()

