import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import plotly.express as px

HitSongs = pd.read_csv('HitSongs.csv')

# Here is out first plot. This is a scatter plot comparing the danceability and energy of the songs.
# Please hover your mouse over the points on this plot to see what song is represented by that plot point! 

fig, ax = plt.subplots()
scatter = ax.scatter(HitSongs['danceability'], HitSongs['energy'])
mplcursors.cursor(scatter, hover = True).connect("add", lambda sel: sel.annotation.set_text(f"{HitSongs['song'][sel.index]} by {HitSongs['artists'].iloc[sel.index]}"))
ax.set_title('Danceability and Energy Comparison')
ax.set_xlabel('Danceability')
ax.set_ylabel('Energy')
plt.show()

# Here is the second plot. My goal here is to examine the trends between danceability, energy, and valence, and see their correlation. 

plt.plot(HitSongs['energy'], label ='Energy', color = 'red')
plt.plot(HitSongs['valence'], label = 'Valence', color = 'blue')
plt.plot(HitSongs['danceability'], label = 'Danceability', color = 'purple')
plt.legend()
plt.title('Examining the Trends of Energy, Valence, and Danceability')
plt.xlabel('Number of songs')
plt.ylabel('Energy, Valence, and Danceability')
plt.show()


# Next, I would like to see box plots for all the columns I did calculations on.
# As a reminder, these were dancebility, energy, speechiness, acousticness, valence, and tempo.

HitSongs[['danceability', 'energy', 'speechiness', 'acousticness', 'valence']].boxplot()
plt.xlabel('Song Features')
plt.ylabel('Scale of 0.0 to 1.0')
plt.title('Song Feature Boxplot')
plt.grid(False)
plt.show()


# Interesting! 
# I want to see what kind of histograms these 5 columns will look like and what they will tell us!

HitSongs[['danceability', 'energy', 'speechiness', 'acousticness', 'valence']].hist(figsize = (10, 7))
plt.show()

# This is all for the plots. Please return to the MakingAHit.ipynb file to see my findings!