import requests
import bs4
from urllib.parse import urljoin
import string_utils

res = requests.get(r"https://dnevnik.bg")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
headers = soup.select(".list-of-latest-stories a")
for match in headers:
    title = match.get("title")
    if title is None:
        continue
    print(title)
    print("")
    article_url = urljoin(res.url, match.get('href'))
    article_result = requests.get(article_url)
    soup = bs4.BeautifulSoup(article_result.text, features="html.parser")
    p = soup.select_one("div.article-content > p")
    print(string_utils.format_string(p.getText()))
    print("--")


