# This file defines Movie class which provide a way to store movie information
# Author: Amrita Saha
# Date:   01/14/2018

import webbrowser


class Movie():
    """ This class provide a way to store movie related information """

    # Description:
    #   This is constructor of Movie class
    # Parameters:
    #   movie_title (string): title of the movie
    #   movie_storyline (string): storyline of the movie
    #   poster_image (string): URL of the poster
    #   trailer_youtube (string): URL of the trailer from youtube
    #   trailer_rating (string): URL of rating in IMDB
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, trailer_rating):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = trailer_rating

    # Description:
    #   This function opens the trailer in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
