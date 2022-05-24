from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def update(self):
        pass

    def on_key_pressed(self, key):
        pass

    def on_key_released(self, key):
        pass