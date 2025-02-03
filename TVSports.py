from tv_interface import TVInterface

class TVSports(TVInterface):
    def turn_on(self):
        print("On Sports channel...")
        return self

    def turn_off(self):
        from TVOff import TVOff
        print("turning off...")
        return TVOff(TVSports())

    def button_news(self):
        from TVNews import TVNews
        print("switch to News...")
        return TVNews()

    def button_sports(self):
        print("already in Sports ...")
        return self

    def button_movies(self):
        from TVMovies import TVMovies
        print("switch to Movies...")
        return TVMovies()