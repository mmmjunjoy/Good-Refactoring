# 모듈화 적용하기

# 프로젝트의 규모가 커질 수록 하나의 파일에 모든 코드를 작성하는 것은 복잡성을 키우고 가독성을 떨어뜨립니다. 
# 따라서 기능 별로 파일을 적절하게 분리하고, 이를 가져와 사용하도록 재구성하는 작업이 필요하며, 이를 모듈화라고 합니다.


#파싱해야 하는 html의 종류가 늘어날 수록 그에 해당하는 파싱 함수도 늘어날 것입니다.
# html을 다운받거나, text 파일에 출력하는 함수는 유틸성 함수들입니다. 
# 따라서 이를 적절히 파일로 나누어 준다면, 프로젝트가 더 복잡해지더라도 유연하게 확장할 수 있습니다.

# 1. parser.py

from bs4 import BeautifulSoup


def parse_article_titles(html):
    soup = BeautifulSoup(html, 'lxml')
    article_container = soup.find('ul', class_='type01')
    articles = article_container.findAll('li')
    titles = []
    for article in articles:
        data_table = article.find('dt')
        if not data_table:
            continue
        title = data_table.find('a').text
        titles.append(title)
    return titles
    