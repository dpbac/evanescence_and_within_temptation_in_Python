# Project : The Symphonic Gothic Metal Rock Data 
## Analyzing Evanescence & Within Temptation

Compare and analyze the rock bands, [Evanescence](https://en.wikipedia.org/wiki/Evanescence) and [Within Temptation](https://en.wikipedia.org/wiki/Within_Temptation), using some of the most important skills of a Data Scientist.

[`Notebook 1`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_01_webscraping_Evanescence_Within_Temptation.ipynb) In this notebook I show how to built a Python web scraper using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), applying some simple [Python string methods](https://www.w3schools.com/python/python_strings.asp) as well as other tools to obtain the lyrics from both bands.

[`Notebook 2`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_02_retrieve_Spotify_data-Evanescence_Within_Temptation.ipynb) In this notebook data about both bands, their albums, and tracks (metadata and audio features) are retrieved using Spotify's API. I'll be using Spotipy which is a lightweight Python library for the [Spotify Web API](https://developer.spotify.com/documentation/web-api/). 

To have access to Spotify API is necessary to request you credentials at https://developer.spotify.com/dashboard/login. Use these credentials in `credentials.txt`.

[`Noteboob 3`](https://github.com/dpbac/evanescence_and_within_temptation_in_Python/blob/master/notebook_03_some_NLP-Evanescence_Within_Temptation.ipynb). Here data retrieved through web scraping and using Spotify's API will be used to analyse further both bands. I'll be making use of some NLP and visualizantion.

### Install requirements
* Install requirements using `pip install -r requirements.txt`.
  * Make sure you use Python 3.
  * You may want to use a virtual environment for this.
