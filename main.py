import download
import get_titles
import search_track

if __name__ == '__main__':
    print("Enter your choice:\n 1. Download songs from a Spotify playlist\n 2. Download song by name")
    while True:
        user_choice = input("Choice (1 or 2): ")
        if user_choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if user_choice == '1':
        playlist_link = input("Enter the Spotify playlist URL: ")
        path = input("Enter the path to save the downloaded songs (default: 'downloads'): ")

        titles = get_titles.get_titles(playlist_link)
        ids = search_track.search_youtube_music_ids(titles)

        if any(ids):
            download.download_songs(titles, ids, path)
        else:
            print("No songs found to download.")
    elif user_choice == '2':
        song_name = input("Enter the song name(artist name is optional but recommended): ")
        path = input("Enter the path to save the downloaded song (default: 'downloads'): ")

        ids = search_track.search_youtube_music_ids([song_name])

        if any(ids):
            download.download_songs([song_name], ids, path)
        else:
            print("No song found to download.") 