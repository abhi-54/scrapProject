from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
from time import sleep

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
    url = "https://www.google.com/search?q=" + name + "+mumbai"
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

def getCEO(enterCompanyName):
  sleep(1)
  links = []
  titles = []
  name = str(enterCompanyName)
  if enterCompanyName == None:
    links.append(noneVar)
    titles.append(noneVar)
  else:
    google_url = "https://www.google.com/search?q=ceo+of+" + name + "+linkedin"
    session = HTMLSession()
    response = session.get(google_url).text
    soup = BeautifulSoup(response, 'lxml')
    div_tag = soup.find_all('div', class_='yuRUbf')
    
    for tag in div_tag:
      link = tag.find('a')
      links.append(link.get('href'))
      title = tag.find('h3').text
      titles.append(title)
    session.close()
  final_link = links[0]
  final_title = titles[0]
  return final_link, final_title

def getPhoneAndEmail(enterCompanyURL):
  sleep(1)
  emails = []
  phoneIN_list = []
  if enterCompanyURL == noneVar:
    emails.append(noneVar)
    phoneIN_list.append(noneVar)
  else:
    session = HTMLSession()
    response = session.get(enterCompanyURL).text
    soup = BeautifulSoup(response, 'lxml') 
    
    phoneIN = re.findall(r"(^[6-9]\d{9})$|(\+91[-\s]\d{10})$|(\+91\d{10})$|(\d[-\s]\d{3}[-\s] \d{3}[-\s]\d{4})$|(\d{4}[-\s]\d{3}[-\s]\d{3})$|(0\d{4}[-\s]\d{6})$|(\+\(\d{2}\)[-\s]\(\d {2}\)-\d{8})$", 
    soup.text, flags = re.M)

    for tuples in phoneIN:
      for phone in tuples:
        if phone == "":
          x = 0
        else:
          phoneIN_list.append(phone)
    
    new_emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup. text, re.I)) # re.I: (ignore case); set --> for removing duplicates
    for tupless in new_emails:
      if tupless in new_emails:
        emails.append(tupless)

    session.close()
  return phoneIN_list, emails

