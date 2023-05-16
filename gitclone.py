import csv
import urllib.request, ssl
import requests
import re 
import os
from os.path import exists
from git import Repo
from my_repo import MyRepo

print("Moikka moi")

# Haetaan API-rajapinnasta data: lista GIT-repoja + s-postiosoitteet
# Edellinen tietorakenteeseen

# Käydään lista läpi ja tarkistetaan, onko jokaiselle s-postille oma kansio. 
# Jos ei, luodaan.

# Käydään käyttäjä kerrallaan läpi
## Jos hakemisto on tyhjä
### Tehdään git clone käyttäjän hakemistoon
### Otetaan status talteen - raportoidaan lopussa
## Jos hakemistossa on tavaraa
### Tehdään git pull käyttäjän hakemistoon
### Otetaan talteen viesti - voidaan lopussa kertoa, mihin oli muutoksia

# Raportoidaan
## Lista kaikista
## Täysin uudet
## Muuttuneet

top_level_url = 'https://records.ithou.fi'
url = 'https://records.ithou.fi/api/course/stec2023-server-cmdb-6'
user = 'admin@tuni.fi'
file = open('./local/local-records-api-pass.txt', "r")
file_passwd = file.read()

passwd = re.sub(r"[\n\t\s ]*", "", file_passwd)

def fetchdata():
    # to avoid verifying ssl certificates
    httpsHa = urllib.request.HTTPSHandler(context= ssl._create_unverified_context())

    # setting up realm+urls+user-password auth
    # (top_level_url may be sequence, also the complete url, realm None is default)
    #### top_level_url = 'https://ip:port_or_domain'
    # of the std managers, this can send user+passwd in one go,
    # not after HTTP req->401 sequence
    password_mgr = urllib.request.HTTPPasswordMgrWithPriorAuth()
    password_mgr.add_password(None, top_level_url, user, passwd, is_authenticated=True)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    # create OpenerDirector
    opener = urllib.request.build_opener(handler, httpsHa)

    # url = top_level_url + '/some_url?some_query...'
    response = opener.open(url)

    print(response.read())
    return


def fetchVer1 ():
    print("Fetching url", url)
    print("Fetching with user", user)
    print("Fetching with passwd", passwd)

    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(username=user, password=passwd))
    return (r.content)

def xx_gitdir(alias, cloneurl):
    print("ALIAS: ", alias, "CLONE: ", cloneurl)
    clonedir = 'clonedir/'+alias
    if (exists(clonedir)):
        print("Dir exists: ",clonedir)
    else:
        Repo.clone_from(cloneurl, clonedir)


print("API GET: ")
#fetchdata()
#csvData = fetchVer1()

tmplist = []

gitsfile='/home/ubu/data-local/LATEST-gits23.csv'

with open(gitsfile, newline='') as csvfile:
    data = csv.DictReader(csvfile)
    cnt = 0
    for row in data:
        #print(row)
        tmplist.append(row)
        cnt += 1                

repo_list = []

for row in tmplist:
    email = row['email']
    cloneurl = row['cloneurl']
    alias = email.replace('@tuni.fi','')    
    myObj = MyRepo(alias, cloneurl)
    repo_list.append(myObj)
    #gitdir(alias, cloneurl)
    if (not myObj.localExists()):
        myObj.clone()
    else:
        myObj.pull()

for obj in repo_list:
    obj.summarize()

