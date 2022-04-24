import requests
from bs4 import BeautifulSoup

url = 'https://jeil.jje.hs.kr/' # 학교 메인 홈페이지 URL

response = requests.get(url)

print("[오늘의 급식]")

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('#container > div.main_content > div.meal_menu > ul > li')
    content = str(content)
    content = content.split('<br>')

    # 불필요한 문자열(HTML TAG) 제거
    for i in content :
        if '<br/>' in i :
            i = i.split("<br/>")
            for j in i :
                if '</br>' in j :
                    print(j.strip("</br></br></li>"))
                elif '</li>' in j :
                    print(j.strip("</li>"))
                else :
                    print(j)
        if '</li>' in i :
            print(i.strip("</li>"))
        elif '<li>' in i :
            print(i[4:])
        

# 크롤러가 웹 사이트에 접근할 수 없다면 status code 출력
else : 
    print(response.status_code)

print("<--------------------------------->")