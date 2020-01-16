# importing packages

import argparse
import sys
import requests
from bs4 import BeautifulSoup



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


# main function

def main():
    
    parser = argparse.ArgumentParser()
    # Multually exlusive arguments (you need to choose one, not both!)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--evanescence", help="provide links to extract lyrics from Evanescence", action="store_true")
    group.add_argument("-w", "--within_temptation", help="provide links to extract lyrics from Evanescence", action="store_true")
    
    args = parser.parse_args()
    
    if args.evanescence:
        urls = ['https://songteksten.net/artist/lyrics/1938/evanescence.html',
       'https://songteksten.net/artist/lyrics/1938/evanescence/page/2.html',
       'https://songteksten.net/artist/lyrics/1938/evanescence/page/3.html']
    
    elif args.within_temptation:
        urls = ['https://songteksten.net/artist/lyrics/320/within-temptation.html',
       'https://songteksten.net/artist/lyrics/320/within-temptation/page/2.html',
       'https://songteksten.net/artist/lyrics/320/within-temptation/page/3.html']
    else:
        sys.exit("Invalid choice.")

    list_links_lyrics_songteksten_net = []

    for url in urls:
        list_links_lyrics_songteksten_net.extend(retrieve_hyperlinks(url))
    
    # removing possible duplicates
    list_links_lyrics_songteksten_net = list(set(list_links_lyrics_songteksten_net))

    
    print('Number of links before filtering:', len(list_links_lyrics_songteksten_net))
#     print('\n')
    
    # filtering hyperlinks which contain lyrics - specific for songteksten.net

    # using url address to filter lyrics

    spliting = urls[0].split('/')
    filter_lyrics = spliting[2]+'/lyric/'+spliting[-2]

    list_links_lyrics_songteksten_net = [link for link in list_links_lyrics_songteksten_net if (filter_lyrics 
                                                                              in link) ]

    print('Number of links after filtering:', len(list_links_lyrics_songteksten_net))
    
    
    
if __name__=='__main__':
    main()