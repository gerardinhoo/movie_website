import fresh_tomatoes
import media

# Six instances associated to the instances variables in media.py.
# media.Movie has been assigned to differents movies...
# media.Movie outputs the storyline, the images and the trailers of the movies.


delta_force = media.Movie("Delta Force",
                               "The Delta Force team are assigned to save the hostages \
                                from the terrorists.",
                               "https://upload.wikimedia.org/wikipedia/en/8/8d/Delta_force_poster.jpg",
                               "https://www.youtube.com/watch?v=r-UCFBS4a5I")

goal = media.Movie("Goal, The Dream Begins",
                               "A talent football player has been given a chance to play pro.",
                               "https://upload.wikimedia.org/wikipedia/en/9/96/GoalPoster.jpg",
                               "https://www.youtube.com/watch?v=67LM5X9-MHA")

scorpions_king = media.Movie("Scorpions King",
                             " A great warrior fights against the ennemies that are \
                              destroying his homeland.",
                             "https://upload.wikimedia.org/wikipedia/en/1/1d/The_Scorpion_King_poster.jpg",
                             "https://www.youtube.com/watch?v=CmEKTae2iys")

the_defender = media.Movie("The Defender", 
                           "A bodyguard well trained from China has been given the job to \
                            protect a businesman's girfriend.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c8/The-Bodyguard-from-Beijing.jpg",
                           "https://www.youtube.com/watch?v=YRqp9op5YXw")

you_got_served = media.Movie("You got served",
                             "Two friends compete together in a though street dance against \
                              others dancers in order to win some money.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b3/You-got-served-poster.jpg",
                             "https://www.youtube.com/watch?v=JkBe80SajCg")

double_impact = media.Movie("Double Impact",
                            "After being separated for quite some time, Two twins are back  \
                             together to avenge their parent's deaths who have been murdered by some criminals.",
                            "https://upload.wikimedia.org/wikipedia/en/2/24/Double_impact.jpg",
                            "https://www.youtube.com/watch?v=6IDVNSO4mt4")

# The variable movies is being defined as a list.

movies = [delta_force, goal, scorpions_king, the_defender, you_got_served, double_impact]
fresh_tomatoes.open_movies_page(movies)





                     
