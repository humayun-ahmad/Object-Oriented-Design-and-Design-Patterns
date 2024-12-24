from abc import ABC, abstractmethod
from video_processor import VideoProcessor

class Video(ABC):
    def __init__(self, processor: VideoProcessor):
        self.processor = processor

    @abstractmethod
    def play(self, video_file: str):
        pass

class YoutubeVideo(Video):
    def play(self, video_file: str):
        print("Playing YouTube video:")
        self.processor.process(video_file)

class NetflixVideo(Video):
    def play(self, video_file: str):
        print("Playing Netflix video:")
        self.processor.process(video_file)
