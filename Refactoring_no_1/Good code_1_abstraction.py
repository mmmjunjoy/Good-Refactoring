#추상화 적용하기

# 변경파트

# 먼저 html 다운로드, 파싱, 텍스트 파일 출력 기능을 각각 함수로 분리하였습니다. 
# 그리고 함수명에서 각각의 기능을 유추할 수 있도록 네이밍을 하였으며, 
# main 함수 역시도 naver_news_titles_crawl 이라는 이름으로 변경하였습니다.

# 장점

#코드를 읽어보면 html을 다운받고, titles를 추출한 다음, 텍스트 파일에 쓰는구나를 알 수 있습니다. 
# 이러한 추상화를 통해서 개발자는 전체 코드의 진행 흐름을 파악하기 편해지며 기능별로 나뉘어져 있기 때문에 디버깅과 유지 보수가 편해집니다.

from bs4 import BeautifulSoup
import requests

def get_html_from_url(url):
    response = requests.text
    return html

def parse_article_titles(html):
    soup = BeautifulSoup(html, 'lxml')
    article_container = soup.find('ui',class_='type01')
    articles = article_container.findAll('li')
    titles = []
    for article in articles:
        data_table = article.find('dt')
        if not data_table:
            continue
        title = data_table.find('a').text
        titles.append(title)
    return titles

def write_titles(titles,filename):
    with open(filename,'w') as result:
        for title in titles:
            result.write(title + '\n')

def naver_news_titles_crawl(keyword):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}'
    html = get_html_from_url(url)
    titles = parse_article_titles(html=html)
    write_titles(titles=titles, filename=f'{keyword}.txt')

if __name__ == '__main__':
    naver_news_titles_crawl(keyword='트와이스')

