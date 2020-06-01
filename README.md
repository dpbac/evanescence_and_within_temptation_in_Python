# Project : The Symphonic Gothic Metal Rock Data 
## Analyzing Evanescence & Within Temptation

Compare and analyze the rock bands, [Evanescence](https://en.wikipedia.org/wiki/Evanescence) and [Within Temptation](https://en.wikipedia.org/wiki/Within_Temptation), 
using some of the most important skills of a Data Scientist.

[`Notebook 1`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_01_webscraping_Evanescence_Within_Temptation.ipynb) In this notebook I show how 
to built a Python web scraper using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), applying some simple [Python string methods](https://www.w3schools.com/python/python_strings.asp) as well as other tools to obtain the lyrics from both bands.

[`Notebook 2`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_02_Spotify_data-Evanescence_Within_Temptation.ipynb) In this notebook 
data about both bands, their albums, and tracks (metadata and audio features) are retrieved using Spotify's API. I'll be using [Spotipy](https://spotipy.readthedocs.io/en/2.12.0/) 
which is a lightweight Python library for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/). In this notebook we
present already some EDA comparing both bands.

To have access to Spotify API is necessary to request you credentials at https://developer.spotify.com/dashboard/login. Use these credentials in `credentials.py`.

[`Notebook 3`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_03_classification_using_audio_features.ipynb) 
Some prediction models are used here on audio features of tracks to predict if a track is from `Evanescence` or `Within Temptation`.
Models used are:
* Knn (k-nearest neighbors)
* Decision Tree
* Random Forest
* Adaboost

Also [AutoML techniques](https://en.wikipedia.org/wiki/Automated_machine_learning) are used to identify ML models in a authomatic way. 
Two open source libraries are used:

* [TPOT](https://epistasislab.github.io/tpot/), an open source automated machine learning library developed at the University of Pennsylvania
* [H20.ai AutoML](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html), a second open source automated machine learning library developed by researchers at H20.ai

[`Noteboob 4`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_04_some_NLP-Evanescence_Within_Temptation.ipynb). Here data retrieved through 
web scraping and using Spotify's API will be used to analyse further both bands. I'll be making use of some NLP and visualizantion.

### Install requirements
* Install requirements using `pip install -r requirements.txt`.
  * Make sure you use Python 3.
  * You may want to use a virtual environment for this.

### Using scripts

Script [webscraping_lyrics.py](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/webscraping_lyrics.py) contains the code explained in 
[`Notebook 1`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_01_webscraping_Evanescence_Within_Temptation.ipynb) to retrieve 
lyrics of Evanescence or Within Temptation from songteksten.net.

#### Use:

Got to the folder where `webscraping_lyrics.py` is located and type the following command depending on which lyrics you need to retrieve:

- to retrieve lyrics from evanescence: `python webscraping_lyrics.py -e`
- to retrieve lyrics from evanescence: `python webscraping_lyrics.py -w`

A subdirectory `data\` will be created to save the resulting files.