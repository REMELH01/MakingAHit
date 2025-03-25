import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

HitSongs = pd.read_csv('HitSongs.csv')

# Here is our first plot. This is a scatter plot comparing the danceability and energy of the songs.
# Please hover your mouse over the points on this plot to see what song is represented by that plot point! 

fig, ax = plt.subplots()
scatter = ax.scatter(HitSongs['danceability'], HitSongs['energy'])
mplcursors.cursor(scatter, hover = True).connect("add", lambda sel: sel.annotation.set_text(f"{HitSongs['song'][sel.index]} by {HitSongs['artists'].iloc[sel.index]}"))
ax.set_title('Danceability and Energy Comparison')
ax.set_xlabel('Danceability')
ax.set_ylabel('Energy')
plt.show()

# Here is the second plot. My goal here is to examine the trends between danceability, energy, and valence, and see their correlation. 

x = np.arange(len(HitSongs))
for column in ['energy', 'valence', 'danceability']:
    y = HitSongs[column]
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), '--', label = f'{column} trendline')
plt.legend()
plt.title('Examining the Trends of Energy, Valence, and Danceability')
plt.xlabel('Number of songs')
plt.ylabel('Energy, Valence, and Danceability')
plt.show()


# Next, I would like to see box plots for all the columns of interest.
# As a reminder, these were dancebility, energy, speechiness, acousticness, valence, and tempo.
# Tempo will have its own plot because of the fact that all the tempos are greater than.

HitSongs[['danceability', 'energy', 'speechiness', 'acousticness', 'valence']].boxplot()
plt.xlabel('Song Features')
plt.ylabel('Scale of 0.0 to 1.0')
plt.title('Song Feature Boxplot')
plt.grid(False)
plt.show()

HitSongs[['tempo']].boxplot()
plt.xlabel('Tempo')
plt.ylabel('Beats per Minute')
plt.title('Song Feature Boxplot - Tempo Only')
plt.grid(False)
plt.show()


# Interesting! 
# I want to see how the histograms of these 6 columns will look like and what they will tell us!

HitSongs[['danceability', 'energy', 'speechiness', 'acousticness', 'valence', 'tempo']].hist(figsize = (10, 7))
plt.show()

# This is all for the plots. Please return to the MakingAHit.ipynb file to see my findings!