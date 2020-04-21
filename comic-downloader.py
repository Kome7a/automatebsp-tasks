#! python 3
# comic-downloader.py - Downloads every comic on xkcd-comics
import requests
import os
import bs4

url = "https://xkcd.com"            # start url
os.makedirs('xkcd', exist_ok=True)  # store comics in xkcd.dir

while not url.endswith("#"):
    # Download comics
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    comic_img = soup.select("#comic img")
    if not comic_img:
        print("Couldn't find image")
    else:
        # Download img
        comic_url = "https:" + comic_img[0].get('src')
        print(f"Dowloading img {comic_url}...")
        res = requests.get(comic_url)
        res.raise_for_status()
        # Save the img to xkcd.dir
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), "wb")
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    # Get Prev button content
    prev_link = soup.select("a[rel=prev]")[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print("Done.")

