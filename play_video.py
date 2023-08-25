import cv2

def play_videos(video_paths):
    video_count = len(video_paths)
    video_captures = [cv2.VideoCapture(video_path) for video_path in video_paths]

    while True:
        frames = []

        for i, cap in enumerate(video_captures):
            ret, frame = cap.read()
            if not ret:
                video_captures[i].set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to the beginning if it ends
                _, frame = cap.read()  # Read the first frame
            frames.append(frame)

        concatenated_frames = cv2.hconcat(frames)
        cv2.imshow("Split Screen", concatenated_frames)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    for cap in video_captures:
        cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_paths = ["C:\\Users\\HP\\Desktop\\New folder\\smart_city\\v1 (1).mp4",
                   "C:\\Users\\HP\\Desktop\\New folder\\smart_city\\v2 (1).mp4"]
    play_videos(video_paths)
