from tv_interface import TVInterface

class TVNews(TVInterface):
    def turn_on(self):
        print("On News channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off...")
        return TVOff(TVNews())

    def button_news(self):
        print("Already on News...")
        return self

    def button_sports(self):
        from TVSports import TVSports
        print("switch to sports...")
        return TVSports()

    def button_movies(self):
        from TVMovies import TVMovies
        print("switch to news...")
        return TVMovies()