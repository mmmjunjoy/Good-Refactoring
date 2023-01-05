# 모듈화를 적용하면서 util.py 생성

import requests


def get_html_from_url(url):
    response = requests.get(url)
    html = response.text
    return html


def write_items(items, filename):

    #write_titles 의 범용성을 넓히기 위하여 이름을 write_items로 변경
    with open(filename, 'w') as result:
        for item in items:
            result.write(item + '\n')
