import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import plotly.express as px

# Here is out first plot. This is a scatter plot comparing the danceability and energy of the songs.
# Please hover your mouse over the points on this plot to see what song is represented by that plot point! 

HitSongs = pd.read_csv('HitSongs.csv')

fig, ax = plt.subplots()
scatter = ax.scatter(HitSongs['danceability'], HitSongs['energy'])
mplcursors.cursor(scatter, hover = True).connect("add", lambda sel: sel.annotation.set_text(f"{HitSongs['song'][sel.index]} by {HitSongs['artists'].iloc[sel.index]}"))
ax.set_title('Danceability and Energy Comparison')
ax.set_xlabel('Danceability')
ax.set_ylabel('Energy')
plt.show()

#Here is the second plot. My goal here is to examine the trends between danceability, energy, and valence, and see their correlation. 

plt.plot(HitSongs['energy'], label ='Energy', color = 'red')
plt.plot(HitSongs['valence'], label = 'Valence', color = 'blue')
plt.plot(HitSongs['danceability'], label = 'Danceability', color = 'purple')
plt.legend()
plt.title('Examining the Trends of Energy, Valence, and Danceability')
plt.xlabel('Number of songs')
plt.ylabel('Energy, Valence, and Danceability')
plt.show()


# 