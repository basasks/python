#################################################################################
# TITLE:            Webscraping Script (Single Level Crawl)                     #
# AUTHOR:           BASASKS                                                     #
# PYTHON VERSION:   Python 3.8.5                                                #
# USAGE:            python3 py07_sc_webscrape01.py                              #
# DEV NOTES:        1. Static main URL, output dirrectory and file              #
#                   2. Correct retrieval at the time of development             #
#                                                                               #
#################################################################################


#####   MODULES

import os
import re
import time
import requests
from bs4 import BeautifulSoup


#####   INITIALIZE VARIABLES

outputdir = "/home/basasks/output/py07/"
outputfile = "/home/basasks/output/py07/fbref_data.txt"
teamurl = "https://fbref.com/en/squads/a6a4e67d/Chelsea-Women-Stats"
header = "name|position|nationalteam|clubteam|npg|npxg|shotstotal|assist|xa|npxg+xa|shotcreatingaction\n"
ls_urls = []


#####   MAIN PROGRAM

# INITIALIZE OUTPUT DIRECTORY AND FILE

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

if os.path.isfile(outputfile):
    os.remove(outputfile)
    
f = open(outputfile, "w")
f.write(header)
f.close()

# BUILD LIST OF PLAYER URLS

response = requests.get(url=teamurl, timeout=5)
soupteam = BeautifulSoup(response.content, 'html.parser')

li_th = soupteam.find_all("tbody")[0].find_all("tr")
for th in li_th:
    p_href = th.find("a").get("href")       
    ls_urls.append("https://fbref.com" + p_href)

# LOOP THROUGH LIST OF URLS

for v_url in ls_urls:

    p_name = ""
    p_position = ""
    p_natteam = ""
    p_club = ""
    p_stat1 = ""
    p_stat2 = ""
    p_stat3 = ""
    p_stat4 = ""
    p_stat5 = ""
    p_stat6 = ""
    p_stat7 = ""

    time.sleep(5)
    response = requests.get(url=v_url, timeout=5)
    soupall = BeautifulSoup(response.content, 'html.parser')    
    
    li_h1 = soupall.find_all("h1", {"itemprop": "name"})
    for h1 in li_h1:
        p_name = h1.get_text().strip()
    
    li_div = soupall.find_all("div", {"itemtype": "https://schema.org/Person"})
    for div in li_div:

        try:
            p_position = div.find_all("p")[-5].get_text().split(sep="\xa0▪\xa0")[0].replace("Position:", "").strip()    
        except:
            p_position = ""
        p_natteam = div.find_all("p")[-2].find_all("a")[0].get_text()       
        p_club = div.find_all('p')[-1].get_text().replace("Club:", "").strip()
    
        soupstats = soupall.find_all("div", id=re.compile("div_scout_summar*")) 
        if (len(soupstats) <= 0) or ("GK" in p_position) :
            p_stat1 = ""
            p_stat2 = ""
            p_stat3 = ""
            p_stat4 = ""
            p_stat5 = ""
            p_stat6 = ""
            p_stat7 = ""
        else:
            p_stat1 = soupstats[0].find_all("td", {"class": "right"})[0].get_text()
            p_stat2 = soupstats[0].find_all("td", {"class": "right"})[1].get_text()
            p_stat3 = soupstats[0].find_all("td", {"class": "right"})[2].get_text()
            p_stat4 = soupstats[0].find_all("td", {"class": "right"})[3].get_text()
            p_stat5 = soupstats[0].find_all("td", {"class": "right"})[4].get_text()
            p_stat6 = soupstats[0].find_all("td", {"class": "right"})[5].get_text()
            p_stat7 = soupstats[0].find_all("td", {"class": "right"})[6].get_text()
    
    row = p_name + "|" + p_position + "|" + p_natteam + "|" + p_club + "|" + p_stat1 + "|" + p_stat2 + "|" + p_stat3 + "|" + p_stat4 + "|" + p_stat5 + "|" + p_stat6 + "|" + p_stat7 + "\n"
    f = open(outputfile, "a")
    f.write(row)
    f.close()