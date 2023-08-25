import cv2

def upgrade_quality(input_path, output_path, new_width, new_height):
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the video codec for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create a VideoWriter object to save the upgraded video in MP4 format
    out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to the desired width and height
        resized_frame = cv2.resize(frame, (new_width, new_height))

        # Write the resized frame to the output video
        out.write(resized_frame)

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

def downgrade_quality(input_path, output_path, decimation_factor):
    cap = cv2.VideoCapture(input_path)

    # Get the video's width, height, and frames per second (fps)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the video codec for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create a VideoWriter object to save the downgraded video in MP4 format
    out = cv2.VideoWriter(output_path, fourcc, fps, (width // decimation_factor, height // decimation_factor))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame using decimation_factor
        resized_frame = cv2.resize(frame, (width // decimation_factor, height // decimation_factor))

        # Write the resized frame to the output video
        out.write(resized_frame)

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

