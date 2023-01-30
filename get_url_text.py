# import module
import requests
from bs4 import BeautifulSoup

# link for extract html data


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata(
    "https://towardsdatascience.com/evolution-of-object-detection-and-localization-algorithms-e241021d8bad")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("p"):
    print(data.get_text())
