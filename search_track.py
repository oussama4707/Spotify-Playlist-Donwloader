from ytmusicapi import YTMusic

yt = YTMusic()

def search_youtube_music_ids(queries):
    ids = []
    for q in queries:
        res = yt.search(q, filter="songs", limit=1)
        if res:
            ids.append(res[0].get('videoId'))
        else:
            ids.append(None)
        
    return ids
