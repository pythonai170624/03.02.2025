from TVMovies import TVMovies
from TVNews import TVNews
from TVSports import TVSports
from tv_interface import TVInterface

class TVOff(TVInterface):

    def __init__(self, prev_state: TVInterface):
        self.prev_state = prev_state

    def turn_on(self):
        print(f'turning on to Prev channel {type(self.prev_state)}...')
        # return self.prev_state.turn_on()
        return self.prev_state

    def turn_off(self):
        print("already off...")
        return self

    def button_news(self):
        print("Turning on to News...")
        return TVNews()

    def button_sports(self):
        print("already in Sports ...")
        return TVSports()

    def button_movies(self):
        print("switch to Movies...")
        return TVMovies()
