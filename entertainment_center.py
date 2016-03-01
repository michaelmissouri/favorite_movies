# -*- coding: utf-8 -*-

# import file fresh_tomatoes from folder movies
import fresh_tomatoes

# import file media from folder movies where class Movie() lives.
import media

# Class Movie initializes through the def __init__ constructor.
# Instance variables of class Movie() lives in the def init constructor.
# Determine how many instances of Movie() you want on your page.
# Instances are initalized by accessing the class Movie.
# The constructor function def init has 4 parameters.
# Pass in the 4 arguments that the instance variables can take.

# First instance of one of my favorite movies.

the_graduate = media.Movie("The Graduate",
                           "Benjamin Braddock (Dustin Hoffman) has just "
                           "finished college and, back at his parents' house, "
                           "he's trying to avoid the one question everyone "
                           "keeps asking: What does he want to do with his "
                           "life?",
                           "http://ecx.images-amazon.com/images/I/41NPqDK1CYL."
                           "_SY355_.jpg",
                           "https://www.youtube.com/watch?v=W_1TIITlm8M")

#Second instance.

butch_cassidy = media.Movie("Butch Cassidy and the Sundance Kid",
                            "The true story of fast-draws and wild rides, "
                            "battles with posses, train and bank robberies, "
                            "a torrid love affair and a new lease on outlaw "
                            "life in far away Bolivia. It is also a character "
                            "study of a remarkable friendship between Butch - "
                            "possibly the most likeable outlaw in frontier "
                            "history - and his closest associate, the fabled, "
                            "ever-dangerous Sundance Kid.",
                            "http://cafmp.com/wp-content/uploads/2012/12/butch"
                            "_cassidy_and_the_sundance_kid-v06-1969.jpg",
                            "https://www.youtube.com/watch?v=X41Ylp02NRs")

# Third instance.

wall_street = media.Movie("Wall Street",
                          "On the Wall Street of the 1980s, Bud Fox "
                          "is a stockbroker full of ambition, doing whatever "
                          "he can to make his way to the top. Admiring the "
                          "power of the unsparing corporate raider Gordon "
                          "Gekko, Fox entices Gekko into mentoring him by "
                          "providing insider trading. As Fox becomes "
                          "embroiled in greed and underhanded schemes, his "
                          "decisions eventually threaten the livelihood of "
                          "his scrupulous father. Faced with this dilemma, "
                          "Fox questions his loyalties.",
                          "http://ia.media-imdb.com/images/M/MV5BMzUzNTI5MDMw"
                          "M15BMl5BanBnXkFtZTgwNjk0MzkxMDE@._"
                          "V1_SX640_SY720_.jpg",
                          "https://www.youtube.com/watch?v=FCctqbRrsBQ")

# Fourth instance.

citizen_kane = media.Movie("Citizen Kane",
                           "When a reporter is assigned to decipher newspaper "
                           "magnate Charles Foster Kane's (Orson Welles) "
                           "dying words, his investigation gradually reveals "
                           "the fascinating portrait of a complex man who "
                           "rose from obscurity to staggering heights",
                           "https://tacomafilmclubannex.files.wordpress.com/"
                           "2014/07/8lt2pyp71fhxu2g3k0iyi3uryyl.jpg",
                           "https://www.youtube.com/watch?v=zyv19bg0scg")

# Fifth instance.

american_psycho = media.Movie("American Psycho",
                              "In New York City in 1987, a handsome, young "
                              "urban professional, Patrick Bateman "
                              "(Christian Bale), lives a second life as a "
                              "gruesome serial killer by night. The cast is "
                              "filled by the detective (Willem Dafoe), the "
                              "fiance (Reese Witherspoon), the mistress "
                              "(Samantha Mathis), the coworker (Jared Leto), "
                              "and the secretary (Chloë Sevigny). This is a "
                              "biting, wry comedy examining the elements that "
                              "make a man a monster.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb"
                              "/6/63/Americanpsychoposter.jpg/220px-"
                              "Americanpsychoposter.jpg",
                              "https://www.youtube.com/watch?v=5YnGhW4UEhc")

# Sixth instance.

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting is twenty years old, and "
                                "already stands out in his rough, "
                                "working-class neighborhood in South Boston. "
                                "He's never been to college, except to scrub "
                                "floors as a janitor at MIT",
                                "http://images.moviepostershop.com/good-will"
                                "-hunting-movie-poster-1997-1020265472.jpg",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

# Create a list below so that instances can be retrieved
# through fresh_tomatoes.py and subsequently fresh_tomatoes.html.

movies = [the_graduate, butch_cassidy, wall_street, citizen_kane,
          american_psycho, good_will_hunting]



fresh_tomatoes.open_movies_page(movies)
