from tv_interface import TVInterface

# Context
class TVRoom:
    def __init__(self, state: TVInterface):
        self.state = state

    def turn_on(self):
        self.state = self.state.turn_on()

    def turn_off(self):
        self.state = self.state.turn_off()

    def button_news(self):
        self.state = self.state.button_news()

    def button_sports(self):
        self.state = self.state.button_sports()

    def button_movies(self):
        self.state = self.state.button_movies()