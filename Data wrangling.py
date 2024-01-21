#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:07:10 2023

@author: School
"""
import pandas as pd

# 1 Lees CSV bestand
filmdata = pd.read_csv("movie_plots.csv")

# 2 Inspecteer data
print(filmdata.head)

# 3 Print aantal films per afkomst
aantal_per_land = filmdata['Origin/Ethnicity'].value_counts()
print(aantal_per_land)

# 4 Selecteer alleen rij met bollywood films
bollywood_film = filmdata[filmdata['Origin/Ethnicity'] == 'Bollywood']

# 5 Selecteer Turkse films na 2000
turks_na_2000 = filmdata[(filmdata['Origin/Ethnicity'] == 'Turkish') & (filmdata['Release Year'] > 2000)]

# 6 Maak een nieuwe df met alleen titel, release jaar, land en plot
new_filmdata_df = filmdata[['Title','Release Year', 'Origin/Ethnicity','Plot']]

# 6.1 verander namen naar:
new_filmdata_df.columns = ['Title', 'Year', 'Origin', 'Plot']

# Extra opdracht(Komt er nog aan)
# 7 Maak nieuwe colom genaamd  "kimono" die waar is als er het woord "Kimono" in staat
#kimono = 