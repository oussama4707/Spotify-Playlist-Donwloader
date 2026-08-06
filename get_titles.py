from spotapi import PublicPlaylist



def get_titles(playlist_url ):
    playlist = PublicPlaylist(playlist_url)
    info = playlist.get_playlist_info(limit=100)  # You can adjust the limit as needed

    tracks = []

    for item in info["data"]["playlistV2"]["content"]["items"]:
        track = item["itemV2"]["data"]

        name = track["name"]
        artist = ", ".join(
            a["profile"]["name"]
            for a in track["artists"]["items"]
        )

        tracks.append(f"{name} {artist}")

    print(f"Tracks in the playlist: {tracks}")
    return tracks

