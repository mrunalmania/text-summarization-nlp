# import re

# lines = []

# text = "ronak navadadasbjsnkfms dsvajdhskfn dsdvshjakfn dctsgdvsahfjd [3] dtaygfkj dewtedwjhj dtdjh [5] sdvhsajkfng dftfhbgnjwrwfj [2]"
# text = text.split()
# for i in text:
#     lines.append(re.sub('\[\d+\]', '', i.strip()))
# print(lines)

# Import packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Specify url of the web page
source = urlopen(
    'https://towardsdatascience.com/evolution-of-object-detection-and-localization-algorithms-e241021d8bad').read()

# Make a soup
soup = BeautifulSoup(source,  'html.parser')
soup

# Extract the plain text content from paragraphs
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))

# Extract text from paragraph headers
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))

# Interleave paragraphs & headers
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)

# Drop footnote superscripts in brackets
text = re.sub(r"\[.*?\]+", '', text)

# Replace '\n' (a new line) with '' and end the string at $1000.
text = text.replace('\n', '')[:-11]
print(text)
