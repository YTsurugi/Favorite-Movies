# -*- coding utf-8 -*-
"""
Created on Sun Jun 18 14:20:07 2017

@author: Sword
"""
import time
import webbrowser
import os

#total_break = 3
#break_count= 0
#print("This program started on"+time.ctime())
#while(break_count < total_break):
#    time.sleep(10)
#    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
#    break_count = break_count +1 


#def rename_files():
#    file_list = os.listdir(r"D:\\test")
#    print(file_list)
#    saved_path = os.getcwd()
#    print("Current Working Directory is "+saved_path)
#    os.chdir(r"D:\\test")    
#    for file_name in file_list:
#        os.rename(file_name, file_name.translate(file_name.maketrans("a","a","1234567890")))
#    os.chdir(saved_path)     

#rename_files()

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

        