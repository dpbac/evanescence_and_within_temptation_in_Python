# importing packages

import argparse
import sys
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

TodaysDate = time.strftime("%Y-%m-%d")

# functions

def retrieve_hyperlinks(main_url):
    """ Extract all hyperlinks in 'main_url' and return a list with these hyperlinks """
    
    # Packages the request, send the request and catch the response: r

    r = requests.get(main_url)

    # Extracts the response as html: html_doc
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc,"lxml")
    
    # Find all 'a' tags (which define hyperlinks): a_tags

    a_tags = soup.find_all('a')
    
    # Create a list with hyperlinks found

    list_links = [link.get('href') for link in a_tags]
    
    # Remove none values if there is some
    
    list_links = list(filter(None, list_links)) 
    
    return list_links


def filter_hyperlinks(urls):
    """ Filter our hyperlinks that are not from lyrics taking into account the structure
    of songteksten.nl website """
    
    list_links_lyrics_songteksten_net = []

    for url in urls:
        list_links_lyrics_songteksten_net.extend(retrieve_hyperlinks(url))
    
    # removing possible duplicates
    list_links_lyrics_songteksten_net = list(set(list_links_lyrics_songteksten_net))

    
    # filtering hyperlinks which contain lyrics - specific for songteksten.net

    # using url address to filter lyrics

    spliting = urls[0].split('/')
    filter_lyrics = spliting[2]+'/lyric/'+spliting[-2]

    list_links_lyrics_songteksten_net = [link for link in list_links_lyrics_songteksten_net if (filter_lyrics 
                                                                              in link) ]
    
    return list_links_lyrics_songteksten_net

def extract_lyric_from_url(url_lyric):
    """ Extract lyrics after prettify beautiful soup from www.songteksten.nl """
    
    
    # send a http request
    r_lyric = requests.get(url_lyric)
    
    # obtain text with html containt of the url
    html_doc_lyric = r_lyric.text
    
    # making html easier to read
    soup_lyric = BeautifulSoup(html_doc_lyric,"lxml")

    
    # prettifying it
    soup_lyric_pretty = soup_lyric.prettify()
    
    # Isolating deal that contains the lyric
    
    text = soup_lyric_pretty.split('</h1>\n')[1].split('<div class="buma-consent" role="alert">')[0]

    # Cleaning text and building a list with it
    list_lyrics = text.split('<br/>\n')
    list_lyrics = [item.replace('\n','') for item in list_lyrics]
    list_lyrics = [item.lstrip().rstrip() for item in list_lyrics]
    
    # removing empty elements from the list
    
    for item in list_lyrics:
        if str(item) == '':
            list_lyrics.remove(item)
            
    # this part was added after noticing that at least one lyric was not following the normal pattern
    
    if '<div' in list_lyrics[0]:
        list_lyrics = list_lyrics[1:]
        
        
    # Having the lyrics in string format
    
    lyrics = '. '.join(list_lyrics)
    
    # returning both list and string
    
    return list_lyrics, lyrics


def build_lyrics_dataframe(list_links_lyrics_songteksten_net,band_name):
    """ Build dataframe with song titles and lyrics from list of lyrics hyperlinks."""

    # building lists with titles of lyrics and lyrics
    list_title_lyrics = []
    list_lyrics = []

    for url_lyric in list_links_lyrics_songteksten_net:
    
        list_title_lyrics.append(url_lyric.split('/')[-1].split('.')[-2])
        list_lyrics.append(extract_lyric_from_url(url_lyric)[1])
        
    df = pd.DataFrame({'song_title': list_title_lyrics,
                  'lyrics': list_lyrics})
    
    # Here we also remove '-' from the title of the songs

    df['song_title'] = df['song_title'].apply(lambda x: x.replace('-',' ').lower())
    
    # saving dataframe to .csv

    df.to_csv("./data/lyrics_"+band_name+"_"+TodaysDate+".csv", index = False)
    
    print("Dataframe with songtitle and lyrics of "+band_name+" created and save in .csv!")

# main function

def main():
    
    # create folder data to save .csv file
    
    if not os.path.exists("./data/"):
        os.mkdir("./data/")
    
    parser = argparse.ArgumentParser()
    # Multually exlusive arguments (you need to choose one, not both!)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--evanescence", help="provide links to extract lyrics from Evanescence", action="store_true")
    group.add_argument("-w", "--within_temptation", help="provide links to extract lyrics from Within Temptation", action="store_true")
    
    args = parser.parse_args()
    
    if args.evanescence:
        urls = ['https://songteksten.net/artist/lyrics/1938/evanescence.html',
       'https://songteksten.net/artist/lyrics/1938/evanescence/page/2.html',
       'https://songteksten.net/artist/lyrics/1938/evanescence/page/3.html']
        band_name = 'Evanescence'
    
    elif args.within_temptation:
        urls = ['https://songteksten.net/artist/lyrics/320/within-temptation.html',
       'https://songteksten.net/artist/lyrics/320/within-temptation/page/2.html',
       'https://songteksten.net/artist/lyrics/320/within-temptation/page/3.html']
        band_name = 'Within_Temptation'
    else:
        sys.exit("Invalid choice.")
        
    
    # obtain hyperlinks that contain lyrics
    list_links_lyrics_songteksten_net = filter_hyperlinks(urls)
    
    # build a dataframe with song titles and lyrics, and save in .csv
    build_lyrics_dataframe(list_links_lyrics_songteksten_net,band_name)
        
        
if __name__=='__main__':
    main()