from video import YoutubeVideo, NetflixVideo
from video_processor import HDProcessor, UHD4KProcessor

if __name__ == "__main__":
    youtube_video = YoutubeVideo(HDProcessor())
    youtube_video.play("abc.mp4")

    netflix_video = NetflixVideo(UHD4KProcessor())
    netflix_video.play("abc.mp4")
