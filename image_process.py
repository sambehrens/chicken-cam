from abc import ABC, abstractmethod


class ImageProcess(ABC):
    @abstractmethod
    def process(self, frame):
        pass
