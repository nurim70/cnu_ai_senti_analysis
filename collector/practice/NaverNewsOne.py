import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/123/0002287820?sid=104'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64 AppleWebkit/537.36 (KHTML, liek Gecko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h2.media_end_head_headline')[0].get_text()

# get_text() : 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백을 제거(실질적으로는 좌우 여백을 없애는거다)
# - 회원가입
content = doc.select('div#dic_area')[0].get_text().strip()
print(f'본문: {title}')  # fstring, 파이썬은 fstring으로 넘어갔다. .format도 있다.
print('내용: {}' .format(content))  # format, 요즘은 다 fstring을 쓴다. 옛날꺼를 알아야지 옛날꺼 만든걸 유지보수 할 수가 있다.