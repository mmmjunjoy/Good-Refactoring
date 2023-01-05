
#네이버 뉴스의 특정 키워드를 검색하여 나온
#기사들의 제목을 추출하여 텍스트 파일에 저장하는 크롤러

#main.py는 알아보기 쉽게 naver_news_crawl로 고침


import parser
import util


def crawl_article_titles(keyword):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}'
    html = util.get_html_from_url(url)
    titles = parser.parse_article_titles(html=html)
    util.write_items(items=titles, filename=f'{keyword}.txt')


if __name__ == '__main__':
    crawl_article_titles(keyword='트와이스')

    #기사 제목을 가져와 텍스트 파일에 출력하는 함수명을 crawl_article_titles로 변경


    # 이를 통해 네이버 뉴스 크롤러에 새로운 기능이 추가된다 하더라도 복잡성의 증가 없이 
    #깔끔하게 확장 할 수 있게 되었다.

