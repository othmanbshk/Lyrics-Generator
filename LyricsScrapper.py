#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:56:17 2021

@author: othman
"""

import lyricsgenius as genius 

file = open("./1PLIKÉ140.txt", "w")  #Change the name of the file you want to write the lyrics on it, depends on the artist(s) you want to work on.
#You can find your creds by creating an account on : https://genius.com/api-clients
creds="YOUR CREDS HERE"
#We are excluding everything that could be a remix, a featuring or a live version, because we want to train our script on the artist.
genius = genius.Genius(creds,
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)", "(Featuring)", "(ft.)", "featuring", "ft.", "avec", "with"],
                             remove_section_headers=True)

artists = ['1PLIKé140'] # You can choose a lot of artists, here we are focusing on one artist to use GPT on his texts


def lyrics_scrapper(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  
    for name in arr:
        try:
            songs = (genius.search_artist(name)).songs #We can also change the script to use it without max_songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <End of the song>   \n \n".join(s))  # Allows us and GPT to restrict the length of the songs.
            c += 1
            print("Songs found:"+ len(s))
        except:  #
            print("No song found")


lyrics_scrapper(artists, 50)






#Thanks to : https://rareloot.medium.com/how-to-download-an-artists-lyrics-from-genius-com-using-python-984d298951c6 for giving the idea of using https://github.com/johnwmillr/LyricsGenius