from urllib.parse import urljoin

from bs4 import BeautifulSoup

from adboard import AdBoardSearch


class YoulaSearch(AdBoardSearch):
    """
    Search for certain query on Youla
    """
    base_url = 'https://youla.ru'

    def __init__(self, query):
        self.query = query

    def set_location(self):
        data = {
            'type': 'point',
            'title': 'Россия, Москва',
            'lat': '55.76',
            'lng': '37.64',
            'r': '0'  # to search beyond 50km
        }

        self.session.post(urljoin(self.base_url, '/web-api/geo/save_location'), data=data)

    def check_new(self):
        url = urljoin(self.base_url, f'?q={self.query}')
        resp = self.session.get(url).text
        return self._extract_ads(resp)

    def _extract_ads(self, html):
        res = []
        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find_all('li', {'class': 'product_item'})
        for i in ads:
            link = i.find('a')
            url = link.get('href')
            title = link.get('title').strip()
            res.append(
                {
                    'url': urljoin(self.base_url, url),
                    'title': title,
                }
            )
        return res
