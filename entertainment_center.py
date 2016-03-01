import fresh_tomatoes
import media

the_graduate = media.Movie("The Graduate",
                        "Benjamin Braddock (Dustin Hoffman) has just finished college and, back at his parents' house, he's trying to avoid the one question everyone keeps asking: What does he want to do with his life?",
                        "http://ecx.images-amazon.com/images/I/41NPqDK1CYL._SY355_.jpg",
                        "https://www.youtube.com/watch?v=W_1TIITlm8M")

avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana)",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=hsdvhJTqLak")

wall_street = media.Movie("Wall Street",
                          "On the Wall Street of the 1980s, Bud Fox is a stockbroker full of ambition, doing whatever he can to make his way to the top.",
                          "http://ia.media-imdb.com/images/M/MV5BMzUzNTI5MDMwM15BMl5BanBnXkFtZTgwNjk0MzkxMDE@._V1_SX640_SY720_.jpg",
                          "https://www.youtube.com/watch?v=FCctqbRrsBQ")

citizen_kane = media.Movie("Citizen Kane", "When a reporter is assigned to decipher newspaper magnate Charles Foster Kane's (Orson Welles) dying words, his investigation gradually reveals the fascinating portrait of a complex man who rose from obscurity to staggering heights",
                             "https://tacomafilmclubannex.files.wordpress.com/2014/07/8lt2pyp71fhxu2g3k0iyi3uryyl.jpg",
                             "https://www.youtube.com/watch?v=zyv19bg0scg")

good_will_hunting = media.Movie("Good Will Hunting", "Will Hunting is twenty years old, and already stands out in his rough, working-class neighborhood in South Boston. He's never been to college, except to scrub floors as a janitor at MIT",
                             "http://images.moviepostershop.com/good-will-hunting-movie-poster-1997-1020265472.jpg",
                             "https://www.youtube.com/watch?v=PaZVjZEFkRs")

midnight_in_paris = media.Movie("Midnight In Paris", "Gil Pender is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee, he has taken to touring the city alone.",
                             "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                             "https://www.youtube.com/watch?v=atLg2wQQxvU")

movies = [the_graduate, avatar, wall_street, citizen_kane, good_will_hunting, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)
