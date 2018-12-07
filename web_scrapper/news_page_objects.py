import bs4
import requests

from common import config

class NewsPage:
    
    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._url = url

        self._visit(self._url)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

class HomePage(NewsPage):
     
    def __init__(self, news_site_uid, url):
        #Herencia
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        links_list = []
        #Busca en la configruracion el selector de los enlaces del periodico
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                links_list.append(link)

        return set(link['href'] for link in links_list)


class ArticlePage(NewsPage):
     
    def __init__(self, news_site_uid, url):
        #Herencia
        super().__init__(news_site_uid, url)

    #the properties are used to generate the csv headers also
    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else ''

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else ''

    @property
    def url(self):
        return self._url