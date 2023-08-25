from flask import Flask, render_template, request, jsonify
import os
from video_processing import upgrade_quality, downgrade_quality
from play_video import play_videos  # Import the play_videos function

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'videos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    # Handle video upload and quality options
    video = request.files['video']
    quality_option = request.form['quality_option']

    # Save the uploaded video to the 'videos' folder
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    if quality_option == 'upgrade':
        processed_video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'upgraded_video.mp4')
        upgrade_quality(video_path, processed_video_path, 1280, 720)
    elif quality_option == 'downgrade':
        processed_video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'downgraded_video.mp4')
        downgrade_quality(video_path, processed_video_path, decimation_factor=2)
    else:
        return jsonify({'error': 'Invalid quality option'})

    # Remove the temporary uploaded video
    os.remove(video_path)

    return jsonify({'processed_video_path': processed_video_path})

@app.route('/view_map/<video_filename>')
def view_map(video_filename):
    processed_video_url = f'/videos/{video_filename}'
    return render_template('map.html', video_url=processed_video_url)

@app.route('/play_videos', methods=['GET', 'POST'])
def play_videos_endpoint():
    if request.method == 'POST':
        video_1 = request.files['video1']
        video_2 = request.files['video2']

        video_paths = []
        for video in [video_1, video_2]:
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
            video.save(video_path)
            video_paths.append(video_path)

        play_videos(video_paths)  # Call the play_videos function from play_video.py

        return render_template('video_player.html', video_paths=video_paths)

    return render_template('play_videos.html')

if __name__ == '__main__':
    app.run(debug=True)

