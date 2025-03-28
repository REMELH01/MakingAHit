# Hello there!

This project was created as my capstone project for Code:You!

I have a extensive background in music, as I got my undergraduate degree from 
Eastern Kentucky University in Music Industry. Because of this background, I am 
always interested in the current trends in music and what makes songs popular.


## Overview

That is a question I hope to answer with this project! I want to know: what makes 
a song a hit? I will be comparing data from 2 data sets - one has songs from the 
Billboard Top 100 list, and the other has data that tracks several data points of 
over 1800 songs from Spotify. My goal is to compare the songs that are on both of 
the lists, and use the data from the Spotify Tracks to see what makes a hit? Is 
it how danceable the song is, the energy of the song, how loud it is? Here is to 
seeing if we will find what makes a hit!

Please note - the main notebook file for this project is the MakingAHit.ipynb file.


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

4 - Activate the virtual environment with this:

GitBash

    venv\Scripts\activate

Mac/Linux

    source venv/bin/activate

5a - Install the requirements package.

    pip install -r requirements.txt

5b - You don't have to install the requirements package!
You can just do the following:

    pip install pandas
    pip install matplotlib
    pip install numpy
    pip install mplcursors
    
6 - Select the virtual environment.
Open the Command Pallette (CTRL+Shift+P) on Windows/(Cmd+Shift+P) on Mac.
Type "Python: Select interpreter" and click on it.
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

This project uses several visualizations to aide in the analysis using matplotlib:
1) Danceability and Energy Comparison - compares the columns titled "danceability" and "energy"; hover your mouse over one of the data points to see what song it is!
2) Examining the Trends of Energy, Valence, and Danceabiliy - finds trends comparing the 3 columns named in the plot title.
3) Song Feature Boxplot - boxplots to compare song features of interest that are all on a scale of 0.0 to 1.0.
4) Song Feature Boxplot: Tempo Only - boxplot of the tempo, as it would not fit properly on previous boxplot.
5) Histograms of Song Features of Interest - gives a deeper insight of song features of interest.


## Features Utilized 

| Feature | Description |
| --- | ---|
| Loading Data | Used 2 CSV files from Kaggle |
| Clean and Operate on the data while combining them | Cleaned and preformed a pandas merge on the CSV files, calculated some new values based on the new dataframe |
| Visualize / Present your data | Made 5 matplotlib visualizations to display the data; added a Tableau word cloud of the song genres |
| Best Practices | Utilized a virtual environment AND made a custom data dictionary notebook |
| Interpret your data | Annotated my code throughout the notebook, with final findings at the end of the MakingAHit notebook |

## Tableau Word Cloud of Genres
![Genre Word Cloud](GenreCloud.png)

While we were able to find that grunge is the most popular genre in the combined 
dataset, it doesn't tell us everything about other popular genres! I wanted to 
see what other genres may be trending, and I thought a visually appealing way to 
display data such as that would be in Tableau by making a word cloud! By doing 
this, in addition to the Spotify playlist I made using ranges I found after 
examining my data, I can definitely see a trend of popular genres! Using this 
image, it seems that grunge, country, hard rock, disco, and dance are all 
popular genres in the music industry, and it seems that making a song in one of 
these genres, you may have a better chance of making a hit!

If you would like to view the Tableau for yourself, here is the link:
https://public.tableau.com/views/GenreCloud/Sheet1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

If you hover over the different genres in the word cloud on the Tableau website, 
it will tell you how may songs used that genre!


## Spotify Playlist

Here is the link to the Spotify playlist based on the songs that are within the ranges towards the end of the notebook!
https://open.spotify.com/playlist/66MLykpjuPr5xCbLOJgHvH?si=dhFJTLG5R8ykhjRuFUydzw


## License

All songs are licensed to their original artists and copyright owners.