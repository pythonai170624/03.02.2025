from abc import ABC, abstractmethod

class TVInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def button_news(self):
        pass

    @abstractmethod
    def button_sports(self):
        pass

    @abstractmethod
    def button_movies(self):
        pass