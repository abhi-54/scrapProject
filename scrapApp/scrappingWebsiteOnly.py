from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
from time import sleep

# to display company 'website' only

list_unwanted = ['https://www.justdial.com/', 'https://www.indiamart.com/', 'https://en.wikipedia.org', 'https://www.zaubacorp.com/',
                  'https://www.easyleadz.com/', 'https://www.quickcompany.in/', 'https://www.connect2india.com/', 'https://infoline.com/'
                  'https://www.moneycontrol.com/',]

noneVar = "Provide Company Name"

def getSearchURL(enterCompanyName):
  sleep(1)
  name = str(enterCompanyName)
  if enterCompanyName == None:
    url = noneVar
    contact_url = noneVar
  else:
    url = "https://www.google.com/search?q=" + name 
    contact_url = url + "+contact"
  return url, contact_url

def getCompanyURL(enterSearchURL):
  sleep(1)
  links = []
  if enterSearchURL == noneVar:
    links.append(noneVar)
  else:
    session = HTMLSession()
    response = session.get(enterSearchURL).text
    soup = BeautifulSoup(response, 'lxml')
    div_tag = soup.find_all('div', class_='yuRUbf')
    for a_tag in div_tag:
      link = a_tag.find('a')
      links.append(link.get('href'))
    for j, a in enumerate(list_unwanted):
      for b in links:
        if a in b:
          links.remove(b)
    session.close()
  return links[0]

