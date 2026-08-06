from ytmusicapi import YTMusic

yt = YTMusic()

def search_youtube_music_ids(queries):
    ids = []
    for q in queries:
        res = yt.search(q, filter="songs")
        if res and len(res) > 0 and 'videoId' in res[0]:
            ids.append(res[0]['videoId'])
        else:
            ids.append(None)
        
    return ids

