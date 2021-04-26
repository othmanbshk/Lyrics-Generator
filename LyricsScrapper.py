#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:56:17 2021

@author: othman
"""

import lyricsgenius as genius # https://github.com/johnwmillr/LyricsGenius

file = open("./1PLIKÉ140.txt", "w")  #Change the name of the file you want to write the lyrics on it, depends on the artist(s) you want to work on.
#You can find your creds by creating an account on : https://genius.com/api-clients
genius = genius.Genius('DBnAAslawteOE1lFE-6ZrsXxPuBu1F2y5cm0MzFqiaRsoIGrTDv9iNws9eik-T74',
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

artists = ['1PLIKé140'] # You can choose a lot of artists, here we are focusing on one artist to use GPT on his texts


def lyrics_scrapper(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k)).songs #We can also change the script to use it without max_songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <End of the song>   \n \n".join(s))  # Allows us and GPT to restrict the number of songs.
            c += 1
            print("Songs found:{len(s)}")
        except:  #
            print("No song found for {name}: {c}")


lyrics_scrapper(artists, 50)