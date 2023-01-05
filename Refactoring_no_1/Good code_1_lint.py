#lint란 프로그래밍 언어에서 권장하는 코딩 스타일, 혹은 코딩 컨벤션입니다. 파이썬은 PEP8을 일반적으로 권장합니다. 
# lint를 어긴다고 해서 에러가 나는 것은 아니지만, 이를 잘 지켜주는 것은 중요합니다. 
# lint는 팀원들 간의 코딩 스타일을 통일시켜주고, 잠재적인 에러의 가능성을 줄여주기 때문입니다.


#pip install pylint 
#pylint main.py 의 명령어를 이용하여 코드 문법 검사를 할 수 있다. 

from bs4 import BeautifulSoup
import requests

def main():  
    # 전역으로 선언되어 있었던 변수들을 main이라는 함수 안으로 한번 감싸주었다.
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=리팩토링'
    response = requests.get(url) #Response -> response 로 변수명 변경
    html=response.text 
    soup=BeautifulSoup(html, 'lxml')
    article_container = soup.find('ul',class_=  'type01') 
    #articleContainer 변수명 -> ariticle_container 로 깔끔하게 변경
    articles = article_container.findAll('li')
    #class = 'type01' 이렇게 되어있는 것을 고쳐줌
    title = []
    for article in articles:
        data_table = article.find('dt')
        if not data_table: 
            #추가적으로 if data_table is not None과 같은 문법은 if not data_table로 단순화시켰습니다.
            continue
        title = dt.find('a').text
        titles.append(title)
    with open('result.txt','w') as result:
        for title in titles:
            result.write(title + '\n')