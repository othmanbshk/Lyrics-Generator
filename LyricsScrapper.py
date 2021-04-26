#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:29:32 2021

@author: othman
"""
#Import the nec. libs
import lyricsgenius as genius
import os 
import pandas as pd
#You can find your creds by creating an account on : https://genius.com/api-clients
creds =""
artist_name ="1PLIKÉ140"
api=genius.Genius(creds)
#You can also remove the max_songs, this is just a test
artist = api.search_artist(artist_name, max_songs=5)
os.mknod(artist_name+"_lyrics.txt")
artist.save_lyrics()
Artist=pd.read_json("Lyrics_"+artist_name+".json")

#