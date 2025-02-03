from tv_interface import TVInterface

class TVMovies(TVInterface):
    def turn_on(self):
        print("On movies channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off...")
        return TVOff(TVMovies())

    def button_news(self):
        from TVNews import TVNews
        print("switch to news...")
        return TVNews()

    def button_sports(self):
        from TVSports import TVSports
        print("switch to sports...")
        return TVSports()

    def button_movies(self):
        print("switch to movies...")
        return self