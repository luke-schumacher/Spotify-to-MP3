# Spotify-to-MP3

Here's a Tutorial/Repo which contains the files allowing you to use the extracted CSV from [exportify](https://watsonbox.github.io/exportify) to find and download the matching songs so you have a local copy. Watch out for licensing!

Ensure that you have the following Python libraries installed. Remember you can install them with `pip install libraryname`:

- **pandas**: For working with CSV files.
- **youtube_dl**: For downloading YouTube videos.
- **pytube**: For downloading YouTube videos.
- **moviepy**: For converting video files to audio files.
- **ffmpeg**: Required by moviepy for video processing. [Download ffmpeg](https://ffmpeg.org/download.html#build-windows)

1. After you have downloaded the list from Exportify use the `title_artist_extractor.py` to get the title and artist names from your exported CSV, ensure you change the name of CSV file to the one you have.
2. Use the `yt_link_finder.py` to find the youtube links of the song names, which will be outputted into a new csv. Note you will need to get your own YouTube API which is fairly simple [here](https://blog.hubspot.com/website/how-to-get-youtube-api-key).
3. Use the `downloader.py` to download the mp4 files of the list using your updated CSV.
4. Finally, you can convert the MP4's using the `convertmp3.py` file.

