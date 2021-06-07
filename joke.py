import requests
from bs4 import BeautifulSoup

def get_best_day_joke():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    response = requests.get('http://anekdot.ru/release/anekdot/day/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    joke = soup.find(class_='topicbox', id=True).find(class_='text').get_text()

    return joke

def get_random_joke():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    response = requests.get('http://anekdot.ru/random/anekdot/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    joke = '\n'.join(soup.find(class_='topicbox', id=True).find(class_='text').strings)

    return joke


if __name__=="__main__":
    print(get_best_day_joke())
