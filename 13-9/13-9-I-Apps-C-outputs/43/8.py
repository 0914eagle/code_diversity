
def get_watch_later_list(n, k, watch_later_list):
    # Initialize a dictionary to store the number of videos of each type
    video_types = {}
    for i in range(k):
        video_types[i] = 0
    
    # Iterate through the watch later list and increment the count of each video type
    for video in watch_later_list:
        video_types[video] += 1
    
    # Initialize a minimum number of clicks variable and set it to the total number of videos
    min_clicks = n
    
    # Iterate through the video types and find the minimum number of clicks to watch all videos of the same type
    for video_type in video_types:
        min_clicks = min(min_clicks, video_types[video_type])
    
    return min_clicks

def main():
    n, k = map(int, input().split())
    watch_later_list = list(input())
    print(get_watch_later_list(n, k, watch_later_list))

if __name__ == '__main__':
    main()

