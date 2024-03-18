import csv
from googleapiclient.discovery import build

def search_youtube(query):
    # Set up YouTube Data API
    api_key = "API KEY HERE"  # Replace with your own API key follow the following tutorial https://blog.hubspot.com/website/how-to-get-youtube-api-key
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search for videos matching the query
    request = youtube.search().list(
        part="id",
        q=query,
        type="video",
        maxResults=1
    )
    response = request.execute()

    # Extract the video ID from the response
    if 'items' in response:
        for item in response['items']:
            if 'id' in item and 'videoId' in item['id']:
                video_id = item['id']['videoId']
                return f"https://www.youtube.com/watch?v={video_id}"
    return None

def find_youtube_links(input_csv, output_csv):
    # Open the input CSV file
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        # Initialize list to store YouTube links
        youtube_links = []

        # Iterate over each row in the CSV file
        for row in reader:
            track_name, artist = row
            query = f"{track_name} {artist} audio"  # Append 'audio' for better results
            youtube_link = search_youtube(query)
            youtube_links.append([track_name, artist, youtube_link])

    # Write the YouTube links to the output CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Track Name', 'Artist', 'YouTube Link'])
        writer.writerows(youtube_links)

if __name__ == "__main__":
    input_csv = 'simplified_YOUR_CSV.csv'
    output_csv = 'youtube_links_workout_mix.csv'
    find_youtube_links(input_csv, output_csv)
