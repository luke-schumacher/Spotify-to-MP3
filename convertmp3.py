import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)
    
    for file in files:
        if file.endswith('.mp4'):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace('.mp4', '.mp3'))
            try:
                print(f"Converting {file} to MP3...")
                video_clip = VideoFileClip(input_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(output_path, bitrate='320k')
                audio_clip.close()
                video_clip.close()
                print(f"Converted {file} to MP3")
            except Exception as e:
                print(f"Error converting {file}: {str(e)}")

# Specify the input and output folders
input_folder = 'downloaded_videos'
output_folder = 'downloaded_mp3'

# Convert MP4 files to MP3
convert_mp4_to_mp3(input_folder, output_folder)
