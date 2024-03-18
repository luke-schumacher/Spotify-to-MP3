import csv
from pytube import YouTube

def download_youtube_videos_from_csv(csv_file, output_folder):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                url = row['YouTube Link']
                # Initialize a YouTube object with the video URL
                yt = YouTube(url)
                
                # Select the highest resolution stream
                stream = yt.streams.get_highest_resolution()
                
                # Download the video to the specified output folder
                stream.download(output_folder)
                
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Error downloading {url}: {str(e)}")

# Example usage:
csv_file = 'YOUR_CSV_NAME.csv'
output_folder = "downloaded_videos"

download_youtube_videos_from_csv(csv_file, output_folder)
