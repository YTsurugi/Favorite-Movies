# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 14:20:55 2017

@author: Sword
"""
import fresh_tomatoes
import media

Mission_impossible = media.Movie("Mission impossible III",
                        "A 2006 American action spy film",
                        "https://i.jeded.com/i/mission-impossible-iii-mi-3-mi3.22804.jpg",
                        "https://www.youtube.com/watch?v=qfU4PTG9wB4")

Takeshi_castle = media.Movie("Takeshi's castle",
                        "A Japanese game show that aired between 1986 and 1990",
                        "http://2.bp.blogspot.com/_gNJU6jA0vIc/TIwTECU7hmI/AAAAAAAAADA/90urkSnJ8LA/s1600/Takeshis+Castle+-+Main+image.jpg",
                        "https://www.youtube.com/watch?v=Q9wAORBq0fE")

Titan = media.Movie("Attack on Titan",
                        "Battle between Giant Monster and people",
                        "https://img.cinematoday.jp/a/N0072527/_size_240x/_v_1429241769/main.jpg",
                        "https://www.youtube.com/watch?v=swpaOrubkT0")


Tomb_raider = media.Movie("Tomb Raider",
                        "A media franchise that originated with an action-adventure video game series",
                        "http://i1-news.softpedia-static.com/images/news2/New-Tomb-Raider-Movie-Will-Be-Similar-to-New-Tomb-Raider-Game-2.jpg",
                        "https://www.youtube.com/watch?v=APPOl7Zuz7U")


Totoro = media.Movie("My Neighbor Totoro",
                        "A 1988 Japanese animated fantasy film written and directed by Hayao Miyazaki",
                        "http://livedoor.blogimg.jp/jean_0214/imgs/8/0/80e5635a.jpg",
                        "https://www.youtube.com/watch?v=YbDV_AvckIs")


Yamato = media.Movie("Space Battleship Yamato",
                        "A Japanese science fiction anime series featuring an eponymous spacecraft",
                        "https://images-na.ssl-images-amazon.com/images/I/51-2wfYdv%2BL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=czEmrnRN4MQ")

Kiminonaha = media.Movie("Your Name",
                        "A 2016 Japanese animated drama film",
                        "http://eiga.k-img.com/images/movie/83796/photo/85fda0a0710fdf1e.jpg?1467791679",
                        "https://www.youtube.com/watch?v=k4xGqY5IDBE")

movies = [Mission_impossible, Takeshi_castle, Titan, Tomb_raider, Totoro, Yamato, Kiminonaha]
fresh_tomatoes.open_movies_page(movies)




