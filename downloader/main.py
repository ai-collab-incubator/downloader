from . import YandexDownloader
from .helper import resolve_direct_yandex_url


if __name__ == "__main__":
    CFG_VIDEO_URL  = "https://disk.yandex.ru/i/qW0c5o0duhkt5w" 
    downloader = YandexDownloader()
    downloader.download(CFG_VIDEO_URL, "video_file")