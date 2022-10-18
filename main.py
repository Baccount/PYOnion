# Importing modules

import socks
import socket
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re




# Configuring Socks to use Tor

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

# It is necessary to use Tor for DNS resolution of Onion websites

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

# Using requests package to read in the Hidden Wiki Onion Website on the Darknet

res = requests.get("http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=tor")

# Using beautifulsoup to get the website content into a nice format

soup = BeautifulSoup(res.content, 'html.parser')

# Getting all links out of the soup and deleting None's

links = [link.get('href') for link in soup.find_all('a')]
# get only the onion links using regex



# find all the links similar to the following format /search/search/redirect?search_term=tor&redirect_url=http://someonionaddress.onion
# and extract the onion link from the redirect_url parameter
onion_links = [re.search(r'redirect_url=(.+)', link).group(1) for link in links if re.search(r'redirect_url=(.+)', link)] 

# print the onion links
for link in onion_links:
    print(link)