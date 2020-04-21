import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
play_file = open("Romeo_and_Juliet.txt", "wb")
for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()