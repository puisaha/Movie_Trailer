import webbrowser

class Movie():
    """ This class provide a way to store movie related information """

    #VALID_RATINGS = ["G","PG","PG-13"]
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube,trailer_rating):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = trailer_rating
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
