from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
doc = r.text

def html_parser(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    res0 = soup.find_all('td', 'titleColumn')
    res1 = soup.find_all('td', 'imdbRating')
    with open('250', 'w') as data:
        for i in range(len(res0)):
            movies_name = res0[i].contents[1].contents[0]
            movies_number = res0[i].contents[0].strip()
            movies_year_release = res0[i].contents[3].string
            movies_rate = res1[i].contents[1]['title']
            final_res = '{0:4} {1:70} {2:8} {3:40}'.format(movies_number, movies_name, movies_year_release, movies_rate)
            data.writelines(final_res+'\n')


if __name__ == "__main__":
    html_parser(doc)
