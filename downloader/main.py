from . import FileDownloader
from .helper import resolve_direct_yandex_url


if __name__ == "__main__":
    CFG_VIDEO_URL  = "https://disk.yandex.ru/i/qW0c5o0duhkt5w"
    resolved_yandex_url = resolve_direct_yandex_url(CFG_VIDEO_URL)
    
    downloader = FileDownloader()
    downloader.download(resolved_yandex_url, "video_file")