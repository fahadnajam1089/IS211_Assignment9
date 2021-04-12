#football

from bs4 import BeautifulSoup
import requests

def football_data():
    source = requests.get('https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/?sortcol=pts&sortdir=descending').text
    soup = BeautifulSoup(source, 'lxml')
    rank = 0

    for player in soup.find_all('tr', attrs={'class': 'TableBase-bodyTr'})[:20]:
        line = player.text.split()
        rank = rank + 1
        fname = line[4]
        lname = line[5]
        position = line[2]
        team = line[3]
        #print(players.text.split())
        pointsScored = line[-2]


        print("%s , %s %s , %s, %s , %s"%(rank,fname,lname,position,team,pointsScored))

if __name__== '__main__':
    football_data()