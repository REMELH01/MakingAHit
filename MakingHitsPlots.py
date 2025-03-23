import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import plotly.express as px

HitSongs = pd.read_csv('HitSongs.csv')

fig, ax = plt.subplots()
scatter = ax.scatter(HitSongs['danceability'], HitSongs['energy'])
mplcursors.cursor(scatter, hover = True).connect("add", lambda sel: sel.annotation.set_text(f"{HitSongs['song'][sel.index]} by {HitSongs['artists'].iloc[sel.index]}"))

ax.set_title('Danceability and Energy Comparison')
ax.set_xlabel('Danceability')
ax.set_ylabel('Energy')

plt.show()