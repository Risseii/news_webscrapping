from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

article_tag = soup.find_all(class_="titleline")
print(article_tag)

#obtain one title and one link using selector
#article_tag0 = soup.select_one(selector=".titleline a")
#print(article_tag0)
#print(article_tag0.getText())
#print(article_tag0.get("href"))

#obtain all
article_texts = []
article_links = []
for i in article_tag:
    article_tag_titles = i.find(name="a").getText()
    article_texts.append(article_tag_titles)
    article_link = i.find(name="a").get("href")
    article_links.append(article_link)


article_upvotes = soup.find_all(name="span", class_="score")
article_total_scores = []
for score in article_upvotes:
    article_score = int(score.getText().split()[0]) #only scores and not the text
    article_total_scores.append(article_score)

print(article_texts)
print(article_links)
print(article_total_scores)

#max score
max_score = max(article_total_scores)
print(f"The highest score is {max_score}")
largest_index = article_total_scores.index(max_score)
#print(f"The index of the article with the highest score is {largest_index}")
print(f"The article with the highest score is {article_texts[largest_index]}")

print("----")
#min score
min_score = min(article_total_scores)
print(f"The lowest score is {min_score}")
min_index = article_total_scores.index(min_score)
print(f"The article with the lowest score is {article_texts[min_index]}")


