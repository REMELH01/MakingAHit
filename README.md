# Hello there!

This project was created as my capstone project for Code:You!

I have a fun background in music, as I got my undergraduate degree from Eastern
Kentucky University in music industry. Because of this background, I am always 
interested in the current trends in music and what makes songs popular.


## Overview

This is a question I hope to answer with this project! I want to know: what makes 
a song a hit? I will be comparing data from 2 data sets - one has songs from the 
Billboard Top 100 list, and the other has data that tracks several data points of 
over 1800 songs from Spotify. My goal is to compare the songs that are on both of 
the lists, and use the data from the Spotify Tracks to see what makes a hit? Is 
it how danceable the song is, the energy of the song, how loud it is? Here is to 
seeing if we will find what makes a hit!


## This project utilizes a virtual environment. 
### Here is how you use it:

1a - Clone this repository.
(or)
1b - Open the repository and download as a ZIP file, and extract it to your desired folder.

2 - Open the file with VSCode in the project folder.

3 - Create a virtual environment.

GitBash

    python -m venv venv

Mac/Linux

    python3 -m venv venv

4 - Activate the existing virtual environment with this:

GitBash

    venv\Scripts\activate

Mac/Linux

    source venv/bin/activate

5 - Install the requirements package.

    pip install -r requirements.txt

You don't have to install the requirements package!
You can just do the following:

    pip install pandas
    pip install matplotlib
    pip install numpy
    pip install mplcursors
    pip install plotly

6 - Select the virtual environment.
Open the Command Pallette (CTRL+Shift+P)/(Cmd+Shift+P) on Mac.
Type "Python: Select interpreter".
Select the one that starts with venv.

PLEASE NOTE! - You may get a window saying you need to install an ipykernel to use the notebook. Please download it in order to use the notebook!


## Dataset Sources

Both datasets were sourced from Kaggle.
* https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
* https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs


## Dependencies

This project was made using Python. Here are the following required packages:
* pandas
* matplotlib 
* numpy
* mplcusrors


## Analysis & Visualizations

This project uses several visualizations to aide in the analysis using matplotlib.
1) Danceability and Energy Comparison - compares the columns titled "danceability" and "energy"
2) Examining the Trends of Energy, Valence, and Danceabiliy - finds trends comparing the 3 columns named in the title
3) Song Feature Boxplot - boxplots to compare song features of interest that are all on a scale of 0.0 to 1.0
4) Song Feature Boxplot: Tempo Only - boxplot of the tempo, as it would not fit properly on previous boxplot
5) Histograms of Song Features of Interest - gives a deeper insight of popular songs


## Features Utilized 
| Feature | Description |
| --- | ---|
| Loading Data | Used 2 CSV files from Kaggle |
| Clean and Operate on the data while combining them | Cleaned and preformed a pandas merge on the CSV files |
| Visualize / Present your data | Made 5 matplotlib visualizations to display the data |
| Best Practices | Utilized a virtual environment AND made a custom data dictionary |
| Interpret your data | Annotated my code throughout the notebook, with final findings at the end of the notebook |


## Spotify Playlist

Here is the link to the Spotify playlist based on the songs that are within the ranges at the end of the notebook!
https://open.spotify.com/playlist/66MLykpjuPr5xCbLOJgHvH?si=dhFJTLG5R8ykhjRuFUydzw


## License

All songs are licensed to their original artists and copyright owners.