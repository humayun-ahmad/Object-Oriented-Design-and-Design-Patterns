from abc import ABC, abstractmethod

class VideoProcessor(ABC):
    @abstractmethod
    def process(self, video_file: str):
        pass

class HDProcessor(VideoProcessor):
    def process(self, video_file: str):
        print(f"Processing {video_file} in HD quality.")

class UHD4KProcessor(VideoProcessor):
    def process(self, video_file: str):
        print(f"Processing {video_file} in UHD 4K quality.")
