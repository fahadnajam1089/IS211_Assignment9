# nfl

from bs4 import BeautifulSoup
import requests


def nfl_data():
    r = requests.get('http://www.footballlocks.com/nfl_point_spreads.shtml').text
    soup = BeautifulSoup(r, 'lxml')

    match = soup.find('span', {'style': 'font-size:10.0pt;font-family:verdana'}).find('table')
    fav = match.text[143:153]
    spread = match.text[154:156]
    underdog = match.text[159:167]

    print('Favorite      Spread      Underdog')
    print('%s     %s          %s' % (fav, spread, underdog))


if __name__ == "__main__":
    nfl_data()