from urllib.parse import urljoin

from bs4 import BeautifulSoup

from adboard import AdBoardSearch


class AvitoSearch(AdBoardSearch):
    """
    Search for certain query on Avito
    """
    base_url = 'https://www.avito.ru/'

    def __init__(self, query):
        self.query = query

    def check_new(self):
        url = urljoin(self.base_url, f'rossiya?s=104&q={self.query}')  # searching on whole Russia
        resp = self.session.get(url).text
        return self._extract_ads(resp)

    def _extract_ads(self, html):
        res = []
        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find_all('div', {'class': 'item__line'})
        for i in ads:
            link = i.find('a', {'class': 'snippet-link'})
            url = link.get('href')
            title = link.get('title').strip()
            res.append(
                {
                    'url': urljoin(self.base_url, url),
                    'title': title,
                }
            )
        return res
