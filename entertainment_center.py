import media
import Fresh_tomato

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/1200px-Toy_Story_logo.svg.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")
spider_man = media.Movie("Spider_Man",
                         "A american super hero",
                         "http://www.impawards.com/2017/posters/spiderman_homecoming_ver14.jpg",
                         "https://www.youtube.com/watch?v=ii3n7hYQOl4",
                         "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")
inception = media.Movie("Inspection",
                         "A thief,who steals corporate secrets through the use of dream-sharing technology",
                         "https://images-na.ssl-images-amazon.com/images/I/51jG7u1g9VL._SL500_AC_SS350_.jpg",
                         "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")
the_lord_of_the_rings = media.Movie("The lord of the rings",
                                    "The future of civilization rests in the fate of the one ring,which has been lost for centuries",
                                    "https://www.movieartarena.com/imgs/lotr1final.jpg",
                                    "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                    "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")
apocalypto = media.Movie("Apocalypto",
                         "The Mayan kingdom is at the height of its opulence and power but the foundations of the empire are beginning to crumble.",
                         "http://cinema.com/image_lib/9530_035.jpg",
                         "https://www.youtube.com/watch?v=ngWBddVNVZs",
                         "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")

moana = media.Movie("Moana",
                     "A story of a brave girl",
                     "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                     "https://www.youtube.com/watch?v=LKFuXETZUsI",
                    "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")

titanic = media.Movie("Titanic",
                      "A love story",
                      "https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")

up = media.Movie("Up",
                 "A 78 years old ballon salesman, is about to fulfill a lifelong dream",
                 "http://c8.alamy.com/comp/C030TP/carl-fredricksen-movie-poster-up-2009-C030TP.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg",
                 "http://www.imdb.com/title/tt1049413/ratings?ref_=tt_ov_rt")

movies = [inception, spider_man, apocalypto, avatar, moana, titanic, up ,toy_story, the_lord_of_the_rings] # make a list for movies
Fresh_tomato.open_movies_page(movies)

