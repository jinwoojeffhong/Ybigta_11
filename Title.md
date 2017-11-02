#**Crawling**
----
## **Crawling Type**
1. 바로 긁어올 수 있는 웹사이트 
2. 바로 긁어올 수 없는 웹사이트

##**Process**
Step1. 정보를 얻고 싶은 싶은 웹페이지 지정
Step2. 크롤러 생성
Step3. 태그를 이용해 웹페이지에서 원하는 정보만을 크롤


###**Step1. Webpage indication**

- urllib 패키지의 request모듈를 이용하여 urlopen함수를 가져옴.
- urlopen() : webpage를 html 형식으로 반환


----

####**네이버 영화정보 가져오기**
> from urllib.request import urlopen 
> html= urlopen("http://movie.naver.com/movie/running/current.nhn#")

###**Step2. Creating Crawler**

- BeautifulSoup : 크롤러 생성 함수, bs4패키지에서 import 가능
- html_parser : 
	- 어떤 방식으로 crawl을 해올 것인지에 관한 파라미터
	- html_parser는 html 문법으로 불러 오겠다라는 의미



>pip3 install beautifulsoup4
>from bs4 import BeautifulSoup 
>crawler = BeautifulSoup(html, "html_parser")





