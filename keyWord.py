import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
# To get keyword phrases ranked highest to lowest.

def main(url):
    url = "https://www.whitehouse.gov/articles/first-lady-melania-trump-personal-experience-covid-19/"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))

    r = Rake()
    text = text.replace(',', '')
    r.extract_keywords_from_text(text)

    return r.get_ranked_phrases()[0]
