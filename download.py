import os
import re
import yt_dlp


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',  # 320, 192, 128...
    }],
}


def _safe_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', ' ', name)
    return name or '_'


def download_songs(queries, ids, path='downloads'):
    if ids is None:
        ids = []
    if queries is None:
        queries = [''] * len(ids)

    if not path:
        path = 'downloads'

    os.makedirs(path, exist_ok=True)

    for query, video_id in zip(queries, ids):
        if not video_id:
            print(f'Skipping missing video id for query: {query}')
            continue

        output_name = _safe_filename(query) if query else video_id
        output_template = os.path.join(path, f'{output_name}.%(ext)s')

        opts = ydl_opts.copy()
        opts['outtmpl'] = output_template

        url = f"https://www.youtube.com/watch?v={video_id}"
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as exc:
            print(f'Skipping unavailable video {video_id} ({query}): {exc}')

