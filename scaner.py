import requests
from bs4 import BeautifulSoup
import json

def scan():# функция для выполнения сбора данных
    base_url = "http://quotes.toscrape.com/page/{}/"
    all_quotes = []
    page = 1

    while True:
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Страница не доступна.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        if not quotes:
            print(f"Цитаты на странице не найдены.")
            break

        for quote in quotes:
            text = quote.find('span', class_='text').get_text(strip=True)
            author = quote.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

            all_quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })

        page += 1

    # Сохранение данных в JSON файл
    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(all_quotes, f, ensure_ascii=False, indent=4)

  

if __name__ == "__main__":
    scan()
